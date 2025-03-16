# MRSD Software Bootcamp

## About This Course

The MRSD Software Bootcamp aims to equip incoming MRSD students (and other aspiring robotics engineers) with the software skills needed to initiate and complete a robotics project from start to finish. 
Much of this bootcamp is based on [F1Tenth](https://roboracer.ai/) (now `RoboRacer`), sourced from courses taught at [UPenn](https://github.com/f1tenth) and [CMU](https://github.com/f1tenth-cmu). 
Students will learn how to setup development environments (Git, Docker, simulation, etc.), implement various algorithms for the F1Tenth vehicle, incorporate multiple modules into a single system for the vehicle, and test their algorithms in the `F1Tenth-Gym-ROS` simulation. 
It is important to note that the focus of this BootCamp is not learning the algorithm details or mathematics behind them. Although these are important and the BootCamp provides resources to learn about them, the primary objective of this BootCamp is help students *learn the software skills needed to implement them*.

## How to Use This Course

This course is designed as a self-paced, self-guided course. Some sections are accompanied with a set of exercises that you can complete to test your knowledge. Each topic aims to explain the foundational concepts and practical usage of a particular tool or platform, and provide you with the resources you need to learn more. While you can find below a recommended order of topics, you are free to explore the topics in any order you wish, following external and internal hyperlinks as you see fit.

## Recommended Order of Topics

1. Basics
    <ol type="A">
        <li>Linux Basics</li>
        <ol type="a">
            <li><a href="linux/linux-101.md">Introduction</a></li>
            <li><a href="linux/cli-tools.md">Linux CLI Tools</a></li>
            <li><a href="linux/docker.md">Docker</a></li>
            <li><a href="linux/remote-access.md">Remote Access using SSH</a></li>
            <li><a href="documentation/markdown.md">Writing Documentation in Markdown</a></li>
            <li><a href="exercises/job-control.md">Job Control</a></li>
        </ol>
        <li>Development environment (Docker)</li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
        <li>Git and Collaborating</li>
        <ol type="a">
            <li>Basics</li>
            <li>Making your GitHub respository</li>
            <li>Making your first branch</li>
            <li>Making your first issue</li>
        </ol>
        <li>Basic Programming</li>
        <ol type="a">
            <li>List of online resources</li>
        </ol>
        <li>IDEs and Code Editors</li>
        <ol type="a">
            <li>What is VS Code and why use it?</li>
            <li>How to config your project in VS Code</li>
            <li>How to debug in VS Code</li>
        </ol>
        <li>ROS Basics</li>
        <ol type="a">
            <li><a href="ros/ros-101.md">Introduction</a></li>
            <li><a href="ros/ros-getting-started.md">Getting Started with ROS for Robotics</a></li>
            <li><a href="ros/ros-action-server.md">ROS Action Server</a></li>
            <li><a href="reading-sensor-data.md">Reading Sensor Data</a></li>
            <li><a href="ros/ros2_basics.md">ROS2 basics</a></li>
            <li><a href="exercises/docker-ros-chatter.md">Exercise: ROS Docker</a></li>
            <li><a href="exercises/ros2_asgn.md">Exercise: Test your understanding</a></li>
            <li> <a href="game/README.md">ROS and C++ Exercise: AI mechanics for controlling a game</a></li>
            <li><a href="F1Tenth/README.md">ROS2 Exercise: Full stack development with F1Tenth</a></li>
        </ol>
    </ol>

2. Mathematics for Robotics

    *Why include math in a software bootcamp?* While this BootCamp focuses on developing software for robots, a fundamental understanding of math is essential to grasp the algorithms behind robotic systems. Though not the primary focus, this section provides the necessary math foundations to complete exercises effectively and build a strong foundation for robotics engineering.
    <ol type="A">
        <li>(Something that you probably already know)</li>
        <ol type="a">
            <li>Linear Algebra</li>
            <li>Calculus</li>
            <li>Optimization</li>
        </ol>
        <li>Robot kinematics and dynamics (for F1Tenth)</li>
        <ol type="a">
            <li>F1Tenth vehicle kinematics (single track model)</li>
            <li>F1Tenth vehicle dynamics (single track model with linear tire model)</li>
        </ol>
    </ol>

3. Simulation 
    <ol type="A">
        <li>Basics</li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
        <li><code>F1Tenth-Gym-ROS</code></li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
        <li>Custom robot and simulation development in Gazebo</li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
    </ol>

4. Sensor
    <ol type="A">
        <li>Sensor basics</li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
        <li>Sensors in <code>F1Tenth-Gym-ROS</code></li>
        <ol type="a">
            <li>Lidar</li>
            <li>IMU</li>
        </ol>
   </ol>

5. Algorithms
   <ol type="A">
        <li>Mapping algorithms
            <ol type="a">
                <li>SLAM</li>
            </ol>
        </li>
        <li>Localization algorithms
            <ol type="a">
                <li>Particle Filter: AMCL</li>
                <li>EKF (Extended Kalman Filter)</li>
            </ol>
        </li>
        <li>Path planning algorithms
            <ol type="a">
                <li>RRT (Rapidly Exploding Tree)</li>
                <li>RRT*</li>
            </ol>
        </li>
        <li>Control algorithms
            <ol type="a">
                <li>Pure Pursuit</li>
                <li>MPC (Model Predictive Control)</li>
            </ol>
        </li>
        <li>Reinforcement Learning
            <ol type="a">
                <li>Model-based RL</li>
                <li>Model-free RL : integrate Alec’s tutorial into the <code>F1Tenth-Gym-ROS</code> simulation.</li>
            </ol>
        </li>
    </ol>

6. Integrate and Compare Performance
7. Writing a Technical Report

<!-- ### DEPRECATED
1. Linux basics
    - [Introduction](linux/linux-101.md)
    - [Linux CLI Tools](linux/cli-tools.md)
    - [Docker](linux/docker.md)
    - [Remote Access using SSH](linux/remote-access.md)
    - [Writing Documentation in Markdown](documentation/markdown.md)
    - [Job Control](exercises/job-control.md)
2. Version control basics
    - [Introduction](version-control/version-control-basics.md)
    - [Git](version-control/git.md)
    - [Exercise: GitHub](exercises/github.md)
3.  ROS basics
    - [Introduction](ros/ros-101.md)
    - [Getting Started with ROS for Robotics](ros/ros-getting-started.md)
    - [ROS Action Server](ros/ros-action-server.md)
    - [Reading Sensor Data](reading-sensor-data.md)
    - [ROS2 basics](ros/ros2_basics.md)
    - [Exercise: ROS Docker](exercises/docker-ros-chatter.md)
    - [Exercise: Test your understanding](exercises/ros2_asgn.md)
4. [ROS and C++ Exercise: AI mechanics for controlling a game](game/README.md)
5. [ROS2 Exercise: Full stack development with F1Tenth](F1Tenth/README.md) -->

## [RL Car Racing](https://github.com/artrela/RL_Car_Racing/tree/97a08ae8ffca019fe2f20cc5a50658cff0a6548f)
[RL Car Racing](https://github.com/artrela/RL_Car_Racing/tree/97a08ae8ffca019fe2f20cc5a50658cff0a6548f) is an independent course for an introduction to common reinforcement methods (RL) leveraging Gymnasium (formerly OpenAI Gym), developed by Alec Trela. 

## Contributing

If you find a typo or error in the course material, please submit a pull request to the [GitHub repository](https://github.com/roboticsknowledgebase/mrsd-software-bootcamp). If you have a suggestion for a new topic, please open an issue on the repository.
