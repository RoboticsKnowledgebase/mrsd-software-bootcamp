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
For detailed solution to Exercise 1, go to <a href="/ros2_exercises/exercise1_solution.md">Exercise 1 Solution</a>.
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
For detailed solution to Exercise 2, go to <a href="/ros2_exercises/exercise2_solution.md">Exercise 2 Solution</a>.
</details>

## 3: Creating a launch file and a parameter file
**Exercise 3**: create a launch file `lab1_launch.py` that launches both of the nodes we've created. If you want, you could also set the parameter for the `talker` node in this launch file.

<details>
<summary>❗Solution❗</summary>
For detailed solution to Exercise 3, go to <a href="/ros2_exercises/exercise3_solution.md">Exercise 3 Solution</a>.
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

