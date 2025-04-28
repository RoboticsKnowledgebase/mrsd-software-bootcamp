# MRSD Software Bootcamp

## About This Course

The MRSD Software Bootcamp aims to equip incoming MRSD students (and other aspiring robotics engineers) with the software skills needed to initiate and complete a robotics project from start to finish. 
Much of this bootcamp is based on [F1Tenth](https://roboracer.ai/) (now `RoboRacer`), sourced from courses taught at [UPenn](https://github.com/f1tenth) by Dr. Rahul Mangharam and [CMU](https://github.com/f1tenth-cmu) by Dr. John Dolan.
Students will learn how to setup development environments (Git, Docker, simulation, etc.), implement various algorithms for the F1Tenth vehicle, incorporate multiple modules into a single system for the vehicle, and test their algorithms in the `F1Tenth-Gym-ROS` simulation. 

This BootCamp utilizes both Python and C++ to emphasize that the underlying programming concepts remain consistent regardless of the language used. While some sections are written in Python and others in C++, the idea is that if you're comfortable in one, you can apply the same principles in the other. Note that while the BootCamp doesn't dive deeply into programming techniques, Section 1(D) does provide additional resources for those needing further guidance.

Note that some parts of this BootCamp will lead you directly to external links. 

## How to Use This Course

This course is designed as a self-paced, self-guided course. Some sections are accompanied by a set of exercises that you can complete to test your knowledge. Each topic aims to explain the foundational concepts and practical usage of a particular tool or platform and provide you with the resources you need to learn more. While you can find below a recommended order of topics, you are free to explore the topics in any order you wish, following external and internal hyperlinks as you see fit.

Moreover, users are recommended to go over the [RoboticsKnowledgebase](https://roboticsknowledgebase.com/) for additional resources that complement this BootCamp. The [RoboticsKnowledgebase](https://roboticsknowledgebase.com/) contains not only basic knowledge related to software skills needed for robotics but also robotics-project-specific knowledge that starting engineers and students might find useful.

## Recommended Order of Topics

1. Basics
   
   If you are new to software development, start here. It covers a lot of the necessary concepts and skills that are required for software development. 
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
        <li>Version Control and Collaborating through GitHub</li>
        <ol type="a">
            <li><a href="version-control/version-control-basics.md">Version control basics</a></li>
            <li><a href="version-control/git.md">Git Basics</a></li>
            <li><a href="version-control/github.md">GitHub Basics and Exercises</a></li>
            <li><a href="version-control/git_pull_request_exercise.md">Exercise: Pull & Request exercise</a></li>
        </ol>
        <li>Basic Programming</li>
        <ol type="a">
            <li><a href="https://roboticsknowledgebase.com/wiki/robotics-project-guide/choose-a-language/">Choosing a Programming Language for Robotics</a></li>
            <li><a href="documentation/programming_basics.md">Online resources</a></li>
        </ol>
        <li>Code Editors and Custom Workspace for Programming</li>
        <ol type="a">
            <li><a href="https://roboticsknowledgebase.com/wiki/tools/code-editors-introduction-to-vs-code-and-vim/">What is VS Code and why use it?</a></li>
            <li><a href="https://code.visualstudio.com/docs/editor/settings">How to config your workspace in VS Code</a></li>
            <li><a href="https://code.visualstudio.com/docs/editor/debugging">How to debug in VS Code</a></li>
        </ol>
    </ol>

2. Practical Math Tools in Python for Robotics & System Dynamics

    You’ll need a working knowledge of key mathematical tools to implement and debug the algorithms that make robots move, perceive, and plan. The goal of Section 2(A) is not to teach an entire math curriculum, but to equip you with just enough theory — and the right Python libraries — to tackle the coding exercises with confidence. In Section 2(B), we will get into the details of F1Tenth vehicle states & dynamics so that you can implement the algorithms in Section 4. 
    <ol type="A">
        <li>Math tools you’ll lean on every day</li>
        <ol type="a">
            <li><a href="math/linear_algebra_numpy.md">Linear Algebra and <code>NumPy</code></a></li>
            <li><a href="math/calculus_sympy.md">Calculus and <code>SymPy</code></a></li>
            <li><a href="math/optimization_scipy.md">Optimization and <code>SciPy</code></a></li>
        </ol>
        <li>Robot dynamics (for F1Tenth)</li>
        <ol type="a">
            <li><a href="math/system_dynamics.md">System Dynamics</a></li>
            <li><a href="math/f1tenth_vehicle_dynamics.md">F1Tenth Vehicle States & Dynamics (single track model)</a></li>
        </ol>
    </ol>

<!-- 3. Robotics Basics
    <ol type="A">
        <li>Sensing (Perception)</li>
        <ol type="a">
            <li><a href="https://roboticsknowledgebase.com/wiki/sensing/">RoboticsKnowledgebase - Sensing</a></li>
            <li></li>
        </ol>
        <li>Actuation (Motion and Control)</li>
        <ol type="a">
            <li></li>
            <li></li>
        </ol>
   </ol> -->

3. Robotics Basics with <code>F1Tenth-Gym-ROS</code>
    <ol type="A">
        <li><a href="https://roboticsknowledgebase.com/wiki/robotics-project-guide/choose-a-sim/">Simulation Basics</a></li>
        <li><code>F1Tenth-Gym-ROS</code></li>
        <ol type="a">
            <li><a href="simulation/f1tenth_gym_ros_basics.md"><code>F1Tenth-Gym-ROS</code> environment with ROS2</a></li>
            <li><a href="simulation/f1tenth_gym_ros_exercise.md"><code>F1Tenth-Gym-ROS</code> basic exercises</a></li>
        </ol>
        <li>Sensing in <code>F1Tenth-Gym-ROS</code></li>
        <ol type="a">
            <li><a href="https://roboticsknowledgebase.com/wiki/sensing/">RoboticsKnowledgebase - Sensing</a></li>
            <li>Lidar</li>
            <li>IMU</li>
        </ol>
        <li>Actuation in <code>F1Tenth-Gym-ROS</code></li>
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

4. Algorithms
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

5. Integrate and Compare Performance
6. Writing a Technical Report

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
