# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: The command ```source /opt/ros/foxy/setup.bash``` sets up the global ROS 2 environment, while the command ```source install/local_setup.bash``` configures your environment to include packages and executables from your local workspace.

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: The queue_size argument in ROS 2 publishers and subscribers controls the size of the message queue. If the queue is full, the oldest messages in the queue will start to be dropped when new messages arrive. A smaller queue_size can lead to more messages being dropped if the subscriber can't keep up with the rate of incoming messages. A larger queue_size can accommodate more messages in the buffer, reducing the likelihood of dropping messages, but at the cost of potentially increased memory usage and, if the subscriber is very slow, older data being processed.

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: The ```ros2 launch``` command can be used in two ways. The first way is running the launch file directly from the directory where it resides (using ```ros2 launch /path/to/launch_file.py```), and you do not need to rebuild your package after making changes to the launch file. ROS 2 will use the launch file directly from that location. The second way is launching the file as part of the installed package (using ```ros2 launch package_name launch_file_name.py```), and you need to rebuild your package after making changes to the launch file. This is because colcon build installs the launch file into your workspace's install directory, and ros2 launch will use the installed version of the file. Without rebuilding, changes made to the launch file in the source directory will not be reflected in the installed version.
