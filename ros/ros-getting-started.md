# Getting Started with ROS for Robotics

There are several things to consider while getting started with ROS for a robotics project. This guide will help you get started with ROS by providing an overview of the ROS ecosystem and various design considerations.

## ROS 1 vs ROS 2: Which Version Should I Use?

ROS 1 is the original version of ROS, which is currently in maintenance mode. ROS 2 is the next generation of ROS, which is currently under active development. ROS 2 is not backwards compatible with ROS 1, but it is possible to run ROS 1 and ROS 2 nodes side-by-side. ROS 1 and ROS 2 are both supported by the [Open Robotics](https://www.openrobotics.org/) organization.

ROS 2 is the recommended version of ROS for new projects, while ROS 1 is still widely used in existing projects due to its maturity, stability and sheer number of supported packages and robotic platforms. That said, ROS 2 is quickly catching up in terms of supported packages and platforms, and it is expected that ROS 2 will eventually replace ROS 1 as the de facto standard for robotic software development.

ROS 2 is designed to be more flexible, scalable and secure than ROS 1. It is also designed to be more portable across different hardware platforms and operating systems. Since ROS 1 was designed as a tool for academic and research purposes, it was not designed for secure, safety-critical or real-time systems. ROS 2 is designed to be more suitable for these types of applications.

### 1. ROS 1 Installation

ROS 1 is supported on Ubuntu Linux, OS X, and Windows.

Follow the instructions on the [ROS Noetic installation page](http://wiki.ros.org/noetic/Installation/Ubuntu) to install ROS Noetic on Ubuntu 20.04.

### 2. ROS 2 Installation

ROS 2 is supported on Ubuntu Linux, OS X, Windows, and various embedded platforms.

Follow the instructions on the [ROS 2 Foxy installation page](https://docs.ros.org/en/foxy/Installation.html) to install ROS 2 Foxy on Ubuntu 20.04.

## ROS Docker vs ROS Native: Which Installation Method Should I Use?

Typically ROS is installed directly as a software on top of your existing operating system (host OS) and runs natively on your machine. However, it is also possible to run ROS inside a Docker container. This section will help you decide which installation method is best for your project.

### But What is Docker?

Docker is a platform to develop, deploy, and run applications with containers. The use of Linux containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

Containerization is increasingly popular because containers are:

- Flexible: Even the most complex applications can be containerized.
- Lightweight: Containers leverage and share the host kernel.
- Interchangeable: You can deploy updates and upgrades on-the-fly.
- Portable: You can build locally, deploy to the cloud, and run anywhere.
- Scalable: You can increase and automatically distribute container replicas.
- Stackable: You can stack services vertically and on-the-fly

For more details on Docker, see [the page on docker](../linux/docker.md)

### ROS Docker

ROS Docker is a Docker image that contains ROS and all of its dependencies. It is designed to be used with Docker, which is a containerization technology that allows you to run applications in isolated environments called containers. Docker containers are lightweight, portable, and secure. They can be used to run applications on any platform that supports Docker, including Linux, OS X, and Windows.

Docker provides a consistent development environment across different platforms, which makes it easier to share code between different platforms.

### Pros and Cons of ROS Docker

Pros:

- Docker containers are lightweight, portable, and secure.
- Docker provides a consistent development environment across different platforms.
- Docker containers can be used to run applications on any platform that supports Docker, including Linux, OS X, and Windows.

Cons:

- Docker containers require more resources than native applications.
- Networking issues are more difficult to debug in Docker containers.
- Hardware access is more difficult in Docker containers because of the number of layers between the hardware and the application. (hardware <-> host OS <-> Docker container <-> application)

### When Should I Use ROS Docker?

You should use ROS Docker if:

- You want to run ROS on a platform that does not support ROS natively, such as a Single Board Computer (SBC).
- You have relatively simple networking requirements.
- You do not extensive and comprehensive hardware access directly from your application.

## References

- [ROS 1 vs ROS 2](https://index.ros.org/doc/ros2/Overview/Concepts/Version-Differences-Between-ROS-1-and-ROS-2/)
- [ROS 1 Installation](http://wiki.ros.org/noetic/Installation/Ubuntu)
- [ROS 2 Installation](https://docs.ros.org/en/foxy/Installation.html)
- [Docker](https://www.docker.com/)
- [ROS Docker](https://hub.docker.com/_/ros)
