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
mkdir -p ~/lab1_ws/src
cd lab1_ws
colcon build
```
Move on to *Section 3* once you're done.

## 2.2 Getting ready **(Docker)**

If you can't have Ubuntu installed natively, install Docker on your system following the instructions here: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/). The documentation of Docker can be found [here](https://docs.docker.com/reference/).

Next, start a container with a bind mount to your workspace directory on your host system inside this repo by:

```bash
docker run -it -v <absolute_path_to_this_repo>/lab1_ws/src/:/lab1_ws/src/ --name ros2_basics ros:foxy
```

This will create a workspace directory on the host at `<absolute_path_to_this_repo>/lab1_ws/src`. It'll create the container based on the official ROS 2 Foxy image, and give the container a name `ros2_basics`. You'll then have access to a terminal inside the container.

`tmux` is recommended when you're working inside a container. It could be installed in the container via: `apt update && apt install tmux`. `tmux` allows you to have multiple `bash` session in the same terminal window. This will be very convenient working inside containers. A quick reference on how to use tmux can be found [here](https://www.redhat.com/sysadmin/introduction-tmux-linux). You can start a session with `tmux`. Then you can call different `tmux` commands by pressing `ctrl+B` first and then the corresponding key. For example, to add a new window, press `ctrl+B` first and release and press `c` to create a new window. You can also move around with `ctrl+B` then `n` or `p`. 

A cheatsheet for the original tmux shortcut keys can be found [here](https://tmuxcheatsheet.com/). To know about how to change the configuration of tmux to make it more useable (for example, if you want to toggle the mouse mode on when you start a tmux bash session or change the shortcut keys), you can find a tutorial [here](https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/).

## 3: ROS 2 Basics

Now that we have the access to a ROS 2 environment, let's test out the basic ROS 2 commands. In the terminal, run:

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

