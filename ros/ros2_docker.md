# ROS2 with Docker

## Installing ROS-Foxy on Docker
Say that you are using Windows or macOS, which do not support ROS/ROS2. Or, say that you want to work with `F1Tenth-Gym-ROS`, which uses ROS-Foxy (❗and we definitely do in this Bootcamp❗). In this case, you would need Ubuntu 20.04 to run ROS-Foxy natively. Otherwise, you would need to use Docker.

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

## `Dockerfile` that allows you to build a custom Docker image
When you make a Docker container, you are automatically directed to the `root` directory. When using Ubuntu, it may not be recommended to run everything as `root`. Then, you might want to have a user within the Docker. However, if you delete the Docker container, that user directoy is also gone. 

Also, you probably don't want to specify that the Docker container needs to start from ROS-Foxy all the time when you start a container. 

For these reasons, and many other possible reasons, you can use a `Dockerfile`. A `Dockerfile` is just a plain text file named `Dockerfile` (no file extension) that contains instructions for building a custom Docker image. Think of it like a recipe: it tells Docker how to create a container environment exactly the way you want — e.g., install ROS, create a user, set paths, etc.

1. Make a new folder for your Docker setup
    
    On your host, open terminal and run:
    ```bash
    mkdir -p ~/ros2_docker
    cd ~/ros2_docker
    ```

1. Create the `Dockerfile`

    Inside `~/ros2_docker`, run:
    ```bash
    touch Dockerfile
    vim Dockerfile
    ```
    Paste the following into the file and save it:
    ```vim
    # Start from official ROS Foxy image
    FROM ros:foxy

    # Create a user named 'dino' with a home directory
    RUN useradd -m -s /bin/bash dino \
        && echo "dino ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

    # Switch to that user
    USER dino
    WORKDIR /home/dino

    # Automatically source ROS 2 when shell starts
    RUN echo "source /opt/ros/foxy/setup.bash" >> /home/dino/.bashrc
    ```

1. Build the Docker image

    From the same folder, run:
    ```bash
    docker build -t ros2-foxy-dino .
    ```
    This will:
    
    - download the `ros:foxy` image,
    - create a new user named `dino`,
    - save this as a new image named `ros2-foxy-dino`.

    It may take a few minutes to complete it for the first time.

1. Run a container from this image

    ```bash
    docker run -it --name ros2_foxy_container ros2-foxy-dino
    ```

## Create a reusable ROS2 workspace to be shared between host computer and Docker container

In many cases, it's good to share a local ROS2 workspace into the container so your code and builds are persistent and you can access the ROS2 workspace from your host computer. This could be done through "bind-mounting". 

This is helpful because ❗if you created a workspace inside the container without a bind-mount, and then delete the container, the workspace will be permanently lost❗

1. Create a workspace folder in your host computer
    ```bash
    usr@host:~$ mkdir -p ~/basic_ws/src
    ```

1. Go into the workspace folder in your host computer
    ```bash
    usr@host:~$ cd basic_ws
    ```

1. Run the following to start a Docker container with a directory bound-mounted from the host into the container 
    
    If you're not using an image, run
    ```bash
    usr@host:~/basic_ws$ docker run -it -v /home/usr/basic_ws/:/home/dino/basic_ws/ --name ros2_foxy_basic ros:foxy
    ```
    If you're using an image, run
    ```bash
    usr@host:~/basic_ws$ docker run -it -v /home/usr/basic_ws/:/home/dino/basic_ws --name ros2_foxy_basic ros2-foxy-dino 
    ```
    This does the following:
    - `docker run`: Starts a new Docker container.
    - `-it`: Interactive terminal session (`-i` = interactive, `-t` = allocate a pseudo-TTY).
    - `-v <host_path>:<container_path>`: Bind-mounts a directory from the host into the container. This allows you to share files between your host and container. ❗Note that only the files inside the directory will be shared between your host and container. Everything else lives inside the container❗
    - `--name <container_name>`: Assigns the container a name.
    - `ros:foxy`: Uses the official ROS 2 Foxy Docker image (based on Ubuntu 20.04).

1. Create the workspace in the container
    ```bash
    dino@container:~$ cd /dino/basic_ws/
    dino@container:~/basic_ws$ colcon build
    ```

1. Once the build is complete, you'll see somethings like the following
    ```bash
    dino@container:~/basic_ws$ ll
    total 24
    drwxrwxr-x 6 dino dino 4096 Jun  3 01:23 ./
    drwx------ 1 dino dino 4096 Jun  3 01:22 ../
    drwxr-xr-x 2 dino dino 4096 Jun  3 01:23 build/
    drwxr-xr-x 2 dino dino 4096 Jun  3 01:23 install/
    drwxr-xr-x 3 dino dino 4096 Jun  3 01:23 log/
    drwxrwxr-x 2 dino dino 4096 Jun  3 01:20 src/
    ```

1. Again, to use ROS2 in the container, you need to source it inside the container
    ```bash
    dino@container:~/basic_ws$ source /opt/ros/foxy/setup.bash
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
