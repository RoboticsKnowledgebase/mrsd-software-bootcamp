# Working with Docker

## Docker ROS Workflow Exercise

In this example you're going to run multiple ROS2 nodes in a single Docker container and demonstrate:

- communication over ROS topics running on Docker container
- usage of a single ROS2 container across terminal sessions

The steps are as follows:

1. Follow the [Docker installation instructions](https://docs.docker.com/engine/install/)

1. Pull the ROS2 Humble Docker image from registry

    ```bash
    docker image pull osrf/ros:humble-desktop
    ```

1. Run a Docker container from downloaded image

    ```bash
    docker run -it --rm --name ros-humble-container osrf/ros:humble-desktop
    ```

1. Run talker node:

    ```bash
    ros2 run demo_nodes_cpp listener &
    ```

    > Note: the `&` at the end of the command is to run the node in the background

1. Run listener node:

    ```bash
    ros2 run demo_nodes_cpp talker
    ```

You should now see the messages being exchanged between the two nodes.

## References

- [Running ROS2 nodes in Docker](https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html)
- [Docker CLI documentation](https://docs.docker.com/engine/reference/run/)
- [ROS docker registry](https://hub.docker.com/_/ros/)
