# Working with Docker

## Docker ROS Workflow Exercise

In this example you're going to run multiple ROS2 nodes in a single Docker container and demonstrate:

- communication over ROS topics running on Docker container
- usage of a single ROS2 container across terminal sessions

The steps are as follows:

1. Follow the [Docker installation instructions](https://docs.docker.com/engine/install/)

1. Pull the ROS2 Humble Docker image from registry

    ```bash
    docker image pull ros:humble
    ```

1. Run a Docker container from downloaded image

    ```bash
    docker run -it --rm ros:melodic --name ros-humble-container
    ```

1. Connect a second terminal to the running container by name

    ```bash
    docker exec -it ros-humble-container bash
    ```

1. Run turtlesim ROS node on terminal 1

    ```bash
    ros2 run turtlesim turtlesim_node
    ```

1. Control the turtle on terminal 2

    ```bash
    ros2 run turtlesim turtle_teleop_key
    ```

You should be able to control the turtle on the GUI connected to terminal 1 by pressing the keys on terminal 2.

## References

- [Running ROS2 nodes in Docker](https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html)
- [Docker CLI documentation](https://docs.docker.com/engine/reference/run/)
- [ROS docker registry](https://hub.docker.com/_/ros/)
