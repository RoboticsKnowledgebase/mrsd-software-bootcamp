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

1. (Optional) To delete the container

    First, exit the container:
    ```bash
    exit
    ```
    Then, on your host system, remove it using:
    ```bash
    docker rm ros2_foxy_container
    ```

1. (Optional) To list Docker containers

    If you want to list only the containers that are running
    ```bash
    docker ps
    ```
    If you want to list all containers (running + stopped)
    ```bash
    docker ps -a
    ```

## Create a reusable ROS2 workspace to be shared between host computer and Docker container

In many cases, it's good to share a local ROS2 workspace into the container so your code and builds are persistent and you can access the ROS2 workspace from your host computer. This could be done through "bind-mounting". 

This is helpful because <span style="color: red;">if you created a workspace inside the container without a bind-mount, and then delete the container, the workspace will be permanently lost</span>.

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
    This does the following:
    - `docker run`: Starts a new Docker container.
    - `-it`: Interactive terminal session (`-i` = interactive, `-t` = allocate a pseudo-TTY).
    - `-v <host_path>:<container_path>`: Bind-mounts a directory from the host into the container. This allows you to share files between your host and container. <span style="color: red;">Note that only the files inside the directory will be shared between your host and container. Everything else lives inside the container</span>.
    - `--name <container_name>`: Assigns the container a name.
    - `ros:foxy`: Uses the official ROS 2 Foxy Docker image (based on Ubuntu 20.04).

1. Create the workspace in the container
    ```bash
    root@container:~$ cd /root/basic_ws/
    root@container:~/basic_ws$ colcon build
    ```

1. Once the build is complete, you'll see somethings like the following
    ```bash
    root@container:~/basic_ws$ ll
    total 24
    drwxrwxr-x 6 root root 4096 Jun  3 01:23 ./
    drwx------ 1 root root 4096 Jun  3 01:22 ../
    drwxr-xr-x 2 root root 4096 Jun  3 01:23 build/
    drwxr-xr-x 2 root root 4096 Jun  3 01:23 install/
    drwxr-xr-x 3 root root 4096 Jun  3 01:23 log/
    drwxrwxr-x 2 root root 4096 Jun  3 01:20 src/
    ```

1. Again, to use ROS2 in the container, you need to source it inside the container
    ```bash
    root@container:~/basic_ws$ source /opt/ros/foxy/setup.bash
    ```

## Using `tmux` inside a Docker container
`tmux` is recommended when you're working inside a container. It could be installed in the container via: 
```bash
apt update && apt install tmux
```
`tmux` allows you to have multiple `bash` session in the same terminal window. This will be very convenient working inside containers. A quick reference on how to use tmux can be found [here](https://www.redhat.com/sysadmin/introduction-tmux-linux). You can start a session with `tmux`. Then you can call different `tmux` commands by pressing `ctrl+B` first and then the corresponding key. For example, to add a new window, press `ctrl+B` first and release and press `c` to create a new window. You can also move around with `ctrl+B` then `n` or `p`. 

A cheatsheet for the original tmux shortcut keys can be found [here](https://tmuxcheatsheet.com/). To know about how to change the configuration of tmux to make it more useable (for example, if you want to toggle the mouse mode on when you start a tmux bash session or change the shortcut keys), you can find a tutorial [here](https://www.hamvocke.com/blog/a-guide-to-customizing-your-tmux-conf/).

## References

- [Running ROS2 nodes in Docker](https://docs.ros.org/en/humble/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html)
- [Docker CLI documentation](https://docs.docker.com/engine/reference/run/)
- [ROS docker registry](https://hub.docker.com/_/ros/)
