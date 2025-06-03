# ROS2 exercise

Now, let's get more familiar with ROS2. Here, you shall hop onto this quick exercise where you shall test your learnings so far to create a package by yourself where 2 nodes can communicate with each other

## Learning Goals

- Getting familiar with ROS 2 workflow
- Understanding how to create nodes with publishers, subscribers
- Understanding ROS 2 package structure, files, dependenciees
- Creating launch files

## 1: Creating a Package
**Exercise 1**: create a package named `basic_pkg` in the workspace we created. The package needs to meet these criteria:
- The package supports both `Python` and `C++`.
- The package needs to have the `ackermann_msgs` dependency.
- Both of these can be done by declaring the correct dependencies in `package.xml`.
- If declared properly, the depencies could be installed using `rosdep` as follows :-
  ```bash
  rosdep update --include-eol-distros
  rosdep install -i --from-path src --rosdistro foxy -y
  ```
- Your package folder should be neat. You shouldn't have multiple 'src' folders or unnecessary 'install' or 'build' folders.

<details>
<summary>❗Solution❗</summary>

1. (Optional) Start your container if you're using Docker:

    ```bash
    docker start -ai ros2_foxy_basic
    ```

2. Navigate to your workspace's `src` directory:

    ```bash
    cd /usr/basic_ws/src
    ```

3. Create the package `basic_pkg` with both Python and C++ support and `ackermann_msgs` as a dependency:

    ```bash
    ros2 pkg create basic_pkg \
      --build-type ament_cmake \
      --dependencies rclcpp rclpy ackermann_msgs
    ```

    > 📝 Note: We use `ament_cmake` here to support C++; Python can still be added with a `setup.py` and `ament_python` config if needed.

4. Check your folder structure to make sure it is clean:
    ```bash
    tree /usr/basic_ws -L 2
    ```
    You should **not** see nested `src/`, `build/`, or `install/` directories inside the `src/` folder.

5. Go to the usr of the workspace and install dependencies with `rosdep`:

    ```bash
    cd /usr/basic_ws
    rosdep update --include-eol-distros
    rosdep install -i --from-path src --rosdistro foxy -y
    ```

6. Build the workspace:

    ```bash
    colcon build
    ```

7. Source the workspace to use your package:

    ```bash
    source install/setup.bash
    ```

You have now created a clean, properly structured ROS 2 package named `basic_pkg` that supports both Python and C++ and depends on `ackermann_msgs`.

</details>

## 2: Creating nodes with publishers and subscribers
**Exercise 2**: create two nodes in the package we just created. You can use either `Python` or `C++` for these nodes.

The first node will be named `talker.cpp` or `talker.py` and needs to meet these criteria:
- `talker` listens to two ROS parameters `v` and `d`.
- `talker` publishes an `AckermannDriveStamped` message with the `speed` field equal to the `v` parameter and `steering_angle` field equal to the `d` parameter, and to a topic named `drive`.
- `talker` publishes as fast as possible.
- To test node, set the two ROS parameters through command line, a launch file, or a yaml file.

The second node will be named `relay.cpp` or `relay.py` and needs to meet these criteria:
- `relay` subscribes to the `drive` topic.
- In the subscriber callback, take the speed and steering angle from the incoming message, multiply both by 3, and publish the new values via another `AckermannDriveStamped` message to a topic named `drive_relay`.

<details>
<summary>❗Solution❗</summary>

Here, we are using Python. For C++, the idea should be the same.

1. Navigate to your package folder
    ```bash
    cd /usr/basic_ws/src/basic_pkg
    ```

1. Create a `scripts/` directory and add Python nodes
	```bash
	mkdir -p scripts
	cd scripts
	```

1. Create `talker.py`
	```python
	#!/usr/bin/env python3
	import rclpy
	from rclpy.node import Node
	from ackermann_msgs.msg import AckermannDriveStamped

	class Talker(Node):
		def __init__(self):
			super().__init__('talker')
			# Declare parameters "v" and "d" with defaults
			self.declare_parameter('v', 0.0)
			self.declare_parameter('d', 0.0)

			self.publisher = self.create_publisher(
				AckermannDriveStamped, 'drive', 10)
			# Publish as fast as possible (timer callback interval = 0 seconds)
			self.timer = self.create_timer(0.0, self.timer_callback)

		def timer_callback(self):
			# Read parameters each cycle
			v = self.get_parameter('v').get_parameter_value().double_value
			d = self.get_parameter('d').get_parameter_value().double_value

			msg = AckermannDriveStamped()
			msg.header.stamp = self.get_clock().now().to_msg()
			msg.drive.speed = float(v)
			msg.drive.steering_angle = float(d)

			self.get_logger().info(
				f'Publishing drive → speed={v:.2f}, steering_angle={d:.2f}')
			self.publisher.publish(msg)

	def main(args=None):
		rclpy.init(args=args)
		node = Talker()
		rclpy.spin(node)
		node.destroy_node()
		rclpy.shutdown()

	if __name__ == '__main__':
		main()
	```
	Then run 
	```bash
	chmod +x talker.py
	```

1. Now, create `relay.py`
	```python
	#!/usr/bin/env python3
	import rclpy
	from rclpy.node import Node
	from ackermann_msgs.msg import AckermannDriveStamped

	class Relay(Node):
		def __init__(self):
			super().__init__('relay')
			self.subscriber = self.create_subscription(
				AckermannDriveStamped,
				'drive',
				self.drive_callback,
				10)
			self.publisher = self.create_publisher(
				AckermannDriveStamped,
				'drive_relay',
				10)

		def drive_callback(self, msg: AckermannDriveStamped):
			out = AckermannDriveStamped()
			out.header.stamp = self.get_clock().now().to_msg()
			out.drive.speed = msg.drive.speed * 3.0
			out.drive.steering_angle = msg.drive.steering_angle * 3.0

			self.get_logger().info(
				f'Relayed → speed={out.drive.speed:.2f}, '
				f'steering_angle={out.drive.steering_angle:.2f}')
			self.publisher.publish(out)

	def main(args=None):
		rclpy.init(args=args)
		node = Relay()
		rclpy.spin(node)
		node.destroy_node()
		rclpy.shutdown()

	if __name__ == '__main__':
		main()
	```
	And run 
	```bash
	chmod +x relay.py
	```

1. Return to `basic_pkg` root and ensure that the following lines are in `CMakeLists.txt`. This is to ensure that the Python scripts are executable under `install/lib/basic_pkg/` by using `ros2 run`. If you prefer to just execute them using `python3`, you may not have to do this.
	```scss
	# Install Python scripts
	install(
	PROGRAMS
		scripts/talker.py
		scripts/relay.py
	DESTINATION lib/${PROJECT_NAME}
	)
	```

1. Build the workspace
	```bash
	colcon build --symlink-install
	```
	Here, `--symlink-install` is optional, but it has some nice benefits. 
	> This creates symbolic links (symlinks) from your build outputs (in `install/`) to the actual source files, instead of copying them. This means that if you change a `.py` file in `src/your_pkg/your_file.py`, the change is immediately reflected, i.e., no rebuild needed. This is useful for Python packages or launch files you edit frequently.

1. Source the workspace
	```bash
	source install/setup.bash
	```

1. (Optional) Run and test the Python nodes
	
	- Make a new tmux session and launch `talker.py` with parameters:
		```bash
		ros2 run basic_pkg talker.py --ros-args -p v:=1.5 -p d:=0.7
		```
	- In a different tmux session, launch `relay.py`:
		```bash
		ros2 run basic_pkg relay.py
		```
	- In a third tmux session, inspect the topics:
		```bash
		ros2 topic echo /drive
		ros2 topic echo /drive_relay
		```
	- You will see `/drive` messages matching `v` and `d`, and `/drive_relay` messages with both fields tripled.
	

</details>

## 3: Creating a launch file and a parameter file
**Exercise 3**: create a launch file `basic_launch.py` that launches both of the nodes we've created. If you want, you could also set the parameters for the `talker` node in this launch file.

<details>
<summary>❗Solution❗</summary>

Here, we are setting the parameters for the `talker` node directly in the launch file. Now, you can also use a `.yaml` file to set the parameters and have the launch file use the parameters in the `.yaml` file if you'd want to. 

1. Navigate to `basic_pkg`
	```bash
	cd /usr/basic_ws/src/basic_pkg
	```

1. Create a `launch/` directory
	```bash
	mkdir -p launch
	cd launch
	```

1. Create `basic_launch.py`
	```bash
	#!/usr/bin/env python3
	from launch import LaunchDescription
	from launch_ros.actions import Node

	def generate_launch_description():
		# Option A: Set parameters directly in the Node constructor:
		talker_node = Node(
			package='basic_pkg',
			executable='talker.py',
			name='talker',
			output='screen',
			parameters=[{'v': 1.5, 'd': 0.7}]
		)

		relay_node = Node(
			package='basic_pkg',
			executable='relay.py',
			name='relay',
			output='screen'
		)

		return LaunchDescription([
			talker_node,
			relay_node
		])
	```
	Then run
	```bash
	chmod +x basic_launch.py
	```
	
1. Return to `basic_pkg` root and update `CMakeLists.txt`
	```bash
	cd /usr/basic_ws/src/basic_pkg
	```
	Open the `CMakeLists.txt` and ensure that it now also includes an install block for launch. For example, you now also need the following block:
	```cmake
	# Install launch files
	install(
		DIRECTORY launch
		DESTINATION share/${PROJECT_NAME}
	)
	```

1. Rebuild the workspace now
	```bash
	colcon build
	```

1. Source the workspace
	```bash
	source install/setup.bash
	```

1. Launch using `ros2 launch`
	```bash
	ros2 launch basic_pkg basic_launch.py
	```

1. In the launch terminal, you should see:
	```bash
	[talker.py-1] [INFO] [1748963618.183552105] [talker]: Publishing drive → speed=1.50, steering_angle=0.70
	[relay.py-2] [INFO] [1748963618.183974980] [relay]: Relayed → speed=4.50, steering_angle=2.10
	```

</details>

## 4: ROS 2 commands

After you've finished all the deliverables, launch the two nodes and test out these ROS 2 commands:
```bash
ros2 topic list
ros2 topic info /drive
ros2 topic echo drive
ros2 node list
ros2 node info /talker
ros2 node info /relay
```

## 5: Test your concepts
Answer the questions listed in [QUESTIONS.md](QUESTIONS.md). The solutions are given in [SOLUTIONS.md](SOLUTIONS.md), please self-assess yourself to verify if your understanding is clear.

