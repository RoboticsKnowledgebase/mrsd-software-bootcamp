# Intro to ROS 2

## Learning Goals

- Getting familiar with ROS 2 workflow
- Understanding how to create nodes with publishers, subscribers
- Understanding ROS 2 package structure, files, dependenciees
- Creating launch files

## Before you start
It's highly recommended to install Ubuntu natively on your machine for developement in future using ROS2. However, if it's impossible for you to do so, you can still follow through the tutorials inside Docker containers. In the following instructions, if you have Ubuntu installed natively, ignore directions for using Docker.

## 1. Overview

The goal of this tutorial is to get you familiar with the ROS 2 workflow. You can either write nodes in Python or C++. However, we highly recommend trying out both since this will be the easiest way to get started on a new language, and the workflow in these two languages are slightly different in ROS2 and it's beneficial to understand both.

It'll be helpful to read these tutorials if you're stuck:

[https://docs.ros.org/en/foxy/Tutorials.html](https://docs.ros.org/en/foxy/Tutorials.html)

[https://roboticsbackend.com/category/ros2/](https://roboticsbackend.com/category/ros2/)

## 2.1 Getting ready **(Native Ubuntu)**

Install ROS 2 following the instructions here: [https://docs.ros.org/en/foxy/Installation.html](https://docs.ros.org/en/foxy/Installation.html). Note that ROS-Foxy is only compatible with Ubuntu 20.04. 

Next, create a workspace:
```bash
usr@host:~$ mkdir -p ~/basic_ws/src
usr@host:~$ cd basic_ws
usr@host:~$ colcon build
```
Move on to *Section 3* once you're done.

## 2.2 Getting ready **(Docker)**

If you can't have Ubuntu installed natively, install Docker on your system following the instructions here: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/). The documentation of Docker can be found [here](https://docs.docker.com/reference/), and the documention of ROS2 with Docker can be found [here](/ros/ros2_docker.md#).

Next, start a container with a bind mount to your workspace directory on your host system inside. To do this, follow the instructions [here](/ros/ros2_docker.md#create-a-reusable-ros2-workspace-to-be-shared-between-host-computer-and-docker-container).

## 3: ROS 2 Basics

Now that we have the access to a ROS 2 environment, let's test out the basic ROS 2 commands. In the terminal (either in host, if you followed 2.1, or in container, if you followed 2.2), run:

```bash
source /opt/ros/foxy/setup.bash
ros2 topic list
```
You should see two topics listed:
```bash
/parameter_events
/rosout
```

If you need multiple terminals and you're inside a Docker container, use `tmux`.

Refer to these slides :- [Slides](Intro-to-ROS2.pdf)

