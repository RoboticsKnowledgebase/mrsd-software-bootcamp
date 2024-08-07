# Docker on Linux

## Key Concepts

### What is Docker?

Docker is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. All containers are run by a single operating system kernel and are thus more lightweight than virtual machines. Containers are created from images that specify their precise contents. Images are often created by combining and modifying standard images downloaded from public repositories.

### What is a container?

A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

### What is a Dockerfile?

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using `docker build` users can create an automated build that executes several command-line instructions in succession.

### What is a Docker image?

A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. An image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel. When the Docker user runs an image, it can become one or multiple instances of that container.

### What is a Docker registry?

A Docker registry is a repository for Docker images. Docker clients connect to registries to download ("pull") images for use or upload ("push") images that they have built. Registries can be public or private. Two main public registries are Docker Hub and Docker Cloud.

### What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

### What is Kubernetes?

Kubernetes is an open-source container-orchestration system for automating application deployment, scaling, and management. It was originally designed by Google and is now maintained by the Cloud Native Computing Foundation. It aims to provide a "platform for automating deployment, scaling, and operations of application containers across clusters of hosts". It works with a range of container tools, including Docker.

### How to install Docker?

#### With Docker-ce

This is the standard way of installing docker as recommended on the official docker documentation [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/). This is the only option if you are on windows or macOS. For ubuntu, there is also an option to install docker.io package using Debian easily.

#### With Docker.io package on ubuntu

To install Docker on Ubuntu, run:

```bash
sudo apt update
sudo apt install docker.io
```

Add user to the `docker` group:

```bash
sudo usermod -aG docker ${USER}
```

To check the status of the Docker service, run:

```bash
sudo systemctl status docker
```

To enable Docker to start on boot, run:

```bash
sudo systemctl enable docker
```

## Some basic exercies

PLease refer to this tutorial slides here to get an idea of some commonly used commands on docker: [Slides](docker_tutorial.pdf)

## References

- [Docker | Wikipedia][1]
- [How to Install and Use Docker on Ubuntu 22.04 | Digital Ocean][2]

[1]: https://en.wikipedia.org/wiki/Docker_(software)
[2]: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04
