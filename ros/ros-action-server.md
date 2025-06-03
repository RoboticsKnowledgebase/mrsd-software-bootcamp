# ROS Action Server

❗This is for ROS 1, not ROS 2. We are keeping this for reference to users who want to use ROS 1❗

## What is an Action Server?

An action server is a node that provides an action. An action is a long-running task that can be awaited and provides feedback on progress. Actions are a powerful way for nodes to communicate with each other and await long-running actions while receiving feedback on progress. Actions can be used to perform motor control or locomotion, or any other task that benefits from being awaited (which means that it can be pre-empted) and has definite progress feedback to provide, as opposed to a service which is a one-shot request-response mechanism.

## Overview

In this exercise you will create a ROS action server and client. The action server will be a simple counter that counts from 0 to 9. The action client will request the action server to count digits. Each progress is relayed as feedback back to the client who also prints the result upon completion.

The steps below assume that you have a working understanding of ROS workspace and packages.

It's also assumed that you have already created a ROS workspace called `ros_ws` in your home directory. If you have not, please follow the instructions at [Creating a ROS Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

## Instructions

1. Create a new ROS package called `action_server`:

    ```bash
    cd ~/ros_ws/src
    catkin new_pkg action_server
    ```

1. Create a new action definition file called `Count.action` in the `action_server` package:

    ```bash
    cd ~/ros_ws/src/action_server
    mkdir action
    touch action/Count.action
    ```

1. Edit the `Count.action` file and add the following:

    ```bash
    int32 count
    ---

    int32 result
    ```

1. Edit the `package.xml` file and add the following:

    ```xml
    <build_depend>actionlib_msgs</build_depend>
    <exec_depend>actionlib_msgs</exec_depend>
    ```

1. Edit the `CMakeLists.txt` file and add the following:

    ```cmake
    find_package(actionlib_msgs REQUIRED)
    add_action_files(DIRECTORY action FILES Count.action)
    generate_messages(DEPENDENCIES actionlib_msgs)
    ```

1. Build the `action_server` package:

    ```bash
    cd ~/ros_ws
    catkin build action_server
    ```

1. Create a new ROS package called `action_client`:

    ```bash
    cd ~/ros_ws/src
    catkin new_pkg action_client
    ```

1. Edit the `package.xml` file and add the following:

    ```xml
    <build_depend>actionlib_msgs</build_depend>
    <exec_depend>actionlib_msgs</exec_depend>
    <build_depend>action_server</build_depend>
    <exec_depend>action_server</exec_depend>
    ```

1. Edit the `CMakeLists.txt` file and add the following:

    ```cmake
    find_package(actionlib_msgs REQUIRED)
    find_package(action_server REQUIRED)
    add_action_files(DIRECTORY action FILES Count.action)
    generate_messages(DEPENDENCIES actionlib_msgs)
    ```

1. Build the `action_client` package:

    ```bash
    cd ~/ros_ws
    catkin build action_client
    ```

1. Create a new file called `count_server.py` in the `action_server` package:

    ```bash
    cd ~/ros_ws/src/action_server
    touch scripts/count_server.py
    ```

1. Edit the `count_server.py` file and add the following:

    ```python
    #!/usr/bin/env python

    import rospy
    import actionlib

    from action_server.msg import CountAction, CountGoal, CountResult

    class CountServer(object):
        def __init__(self):
            self._as = actionlib.SimpleActionServer('count', CountAction, execute_cb=self.execute_cb, auto_start=False)
            self._as.start()

        def execute_cb(self, goal):
            r = rospy.Rate(1)
            success = True

            for i in range(0, goal.count):
                if self._as.is_preempt_requested():
                    rospy.loginfo('Preempted')
                    self._as.set_preempted()
                    success = False
                    break

                rospy.loginfo(i)
                r.sleep()

            if success:
                self._as.set_succeeded(CountResult(i))

    if __name__ == '__main__':

        rospy.init_node('count_server')
        server = CountServer()
        rospy.spin()
    ```

1. Make the `count_server.py` file executable:

    ```bash
    chmod +x scripts/count_server.py
    ```

1. Create a new file called `count_client.py` in the `action_client` package:

    ```bash
    cd ~/ros_ws/src/action_client
    touch scripts/count_client.py
    ```

1. Edit the `count_client.py` file and add the following:

    ```python
    #!/usr/bin/env python

    import rospy
    import actionlib

    from action_client.msg import CountAction, CountGoal, CountResult

    def feedback_cb(feedback):
        rospy.loginfo(feedback)

    if __name__ == '__main__':
        rospy.init_node('count_client')
        client = actionlib.SimpleActionClient('count', CountAction)
        client.wait_for_server()

        goal = CountGoal(10)
        client.send_goal(goal, feedback_cb=feedback_cb)

        client.wait_for_result()
        rospy.loginfo(client.get_result())
    ```

1. Make the `count_client.py` file executable:

    ```bash
    chmod +x scripts/count_client.py
    ```

1. Run the `count_server.py` file:

    ```bash
    rosrun action_server count_server.py
    ```

1. In a new terminal, run the `count_client.py` file:

    ```bash
    rosrun action_client count_client.py
    ```

1. You should see the following output:

    ```bash
    [INFO] [1631635475.000000]: 0
    [INFO] [1631635476.000000]: 1
    [INFO] [1631635477.000000]: 2
    [INFO] [1631635478.000000]: 3
    [INFO] [1631635479.000000]: 4
    [INFO] [1631635480.000000]: 5
    [INFO] [1631635481.000000]: 6
    [INFO] [1631635482.000000]: 7
    [INFO] [1631635483.000000]: 8
    [INFO] [1631635484.000000]: 9
    [INFO] [1631635484.000000]: 9
    ```

## Next Steps

## Summary

## Further Reading

- [ROS Actions | ROS Wiki](http://wiki.ros.org/actionlib)
