# ROS2 with Docker

## Installing ROS-Foxy on Docker
Say that you are using Windows or macOS, which do not support ROS/ROS2. Or, say that you want to work with `F1Tenth-Gym-ROS`, which uses ROS-Foxy (<span style="color: red;">and we definitely do in this Bootcamp!</span>). In this case, you would need Ubuntu 20.04 to run ROS-Foxy natively. Otherwise, you would need to use Docker.

For example, the steps are as follows if you are using Ubuntu 22.04:

1. Follow the [Docker installation instructions](https://docs.docker.com/desktop/)

1. Confirm that Docker works by running 
    ```bash
    docker --version
    ```
    If this shows a version, you're good.

1. Pull the ROS-Foxy Docker image.

    Docker Hub has an official image for ROS Foxy based on Ubuntu 20.04. Run:
    ```bash
    docker pull ros:foxy
    ```
    This downloads the base image with:
    
    - Ubuntu 20.04
    - ROS-Foxy pre-installed

1. Start the container (Interactive Terminal)

    Now run the container and enter it:
    ```bash
    docker run -it --name ros2_foxy_container ros:foxy
    ```
    This opens a terminal inside the Ubuntu 20.04 + ROS Foxy container.

1. Source ROS inside the container

    Inside the container, run:
    ```bash
    source /opt/ros/foxy/setup.bash
    ```
    Note that, each time you want to use ROS2, you need the run the command above. 

1. Check if you can use ROS-Foxy

    You can now use ROS-Foxy inside the container. Try:
    ```bash
    ros2 --help
    ```

1. (Optional) Exit and restart

    To exit the container, run:
    ```bash
    exit
    ```
    To restart it later, run:
    ```bash
    docker start -ai ros2_foxy_container
    ```

## Create a reusable ROS2 workspace to be shared between host computer and Docker container

In many cases, it's good to share a local ROS2 workspace into the container so your code and builds are persistent and you can access the ROS2 workspace from your host computer. 

1. Create a workspace folder in your host computer
    ```bash
    usr@host:~$ mkdir -p ~/basic_ws/src
    ```

1. Go into the workspace folder in your host computer
    ```bash
    usr@host:~$ cd basic_ws
    ```

1. Run the following to start a Docker container with a directory bound-mounted from the host into the container
    ```bash
    usr@host:~/basic_ws$ docker run -it -v /usr/basic_ws/:/root/basic_ws/ --name ros2_foxy_basic ros:foxy
    ```

1. Create the workspace in the container
    ```bash
    root@container:~# cd /root/basic_ws/
    root@container:~/basic_ws# colcon build
    ```

1. Once the build is complete, you'll see the following
    ```bash
    root@container:~/basic_ws# ll
    total 24
    drwxrwxr-x 6 root root 4096 Jun  3 01:23 ./
    drwx------ 1 root root 4096 Jun  3 01:22 ../
    drwxr-xr-x 2 root root 4096 Jun  3 01:23 build/
    drwxr-xr-x 2 root root 4096 Jun  3 01:23 install/
    drwxr-xr-x 3 root root 4096 Jun  3 01:23 log/
    drwxrwxr-x 2 root root 4096 Jun  3 01:20 src/
    ```


## References

- [Running ROS2 nodes in Docker](https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html)
- [Docker CLI documentation](https://docs.docker.com/engine/reference/run/)
- [ROS docker registry](https://hub.docker.com/_/ros/)
