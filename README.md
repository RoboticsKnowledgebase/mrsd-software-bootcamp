# MRSD Software Bootcamp

## About This Course

The MRSD Software Bootcamp aims to equip incoming MRSD students (and other aspiring robotics engineers) with the software skills needed to initiate and complete a robotics project from start to finish. 
Much of this Bootcamp is based on [F1Tenth](https://roboracer.ai/) (now `RoboRacer`), sourced from courses taught at [UPenn](https://github.com/f1tenth) by Dr. Rahul Mangharam and [CMU](https://github.com/f1tenth-cmu) by Dr. John Dolan.
Students will learn how to setup development environments (Git, Docker, simulation, etc.), implement various algorithms for the F1Tenth vehicle, incorporate multiple modules into a single system for the vehicle, and test their algorithms in the `F1Tenth-Gym-ROS` simulation. 

This Bootcamp utilizes both Python and C++ to emphasize that the underlying programming concepts remain consistent regardless of the language used. While some sections are written in Python and others in C++, the idea is that if you're comfortable in one, you can apply the same principles in the other. 

> Note that while the Bootcamp doesn't dive deeply into programming techniques, Section 1(D) does provide additional resources for those needing further guidance.

Note that some parts of this Bootcamp will lead you directly to external links. 

## How to Use This Course

This course is designed as a self-paced, self-guided course. Some sections are accompanied by a set of exercises that you can complete to test your knowledge. Each topic aims to explain the foundational concepts and practical usage of a particular tool or platform and provide you with the resources you need to learn more. While you can find below a recommended order of topics, you are free to explore the topics in any order you wish, following external and internal hyperlinks as you see fit.

Moreover, users are recommended to go over the [RoboticsKnowledgebase](https://roboticsknowledgebase.com/) for additional resources that complement this Bootcamp. The [RoboticsKnowledgebase](https://roboticsknowledgebase.com/) contains not only basic knowledge related to software skills needed for robotics but also robotics-project-specific knowledge that starting engineers and students might find useful.

\* If you want to get some hands-on experience with introductory material on reinforcement learning, go to [RL Car Racing](#rl-car-racing)!

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
            <li><a href="linux/job-control.md">Job Control</a></li>
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
            <li><a href="basic_programming/programming_basics.md">Online resources</a></li>
            <li><a href="basic_programming/markdown.md">Writing Documentation in Markdown</a></li>
        </ol>
        <li>Code Editors and Custom Workspace for Programming</li>
        <ol type="a">
            <li><a href="https://roboticsknowledgebase.com/wiki/tools/code-editors-introduction-to-vs-code-and-vim/">What is VS Code and why use it?</a></li>
            <li><a href="https://code.visualstudio.com/docs/editor/settings">How to config your workspace in VS Code</a></li>
            <li><a href="https://code.visualstudio.com/docs/editor/debugging">How to debug in VS Code</a></li>
        </ol>
        <li>ROS/ROS2 Basics</li>
        <blockquote>
        Please note that the latter part of the Bootcamp utilizes ROS 2 for `F1Tenth`. Furthermore, ROS2 is the preferred ROS version in most of industry and research nowadays. Thus, while some part of the Bootcamp talks about ROS, ❗<span style="color: red; font-weight: bold;">please only install ROS2, specifically ROS-Foxy, for the Bootcamp. For ROS-Foxy, you need Ubuntu 20.04, otherwise, please use Docker containers</span>❗ The topics in section "Basics" that contain "ROS" instead of "ROS2" are for ROS1. We are keeping those as reference for users who want to use ROS1 for their projects.
        </blockquote>
        <ol type="a">
            <li><a href="ros/ros-101.md">Introduction</a></li>
            <li><a href="ros/ros-getting-started.md">Getting Started with ROS/ROS2 for Robotics</a></li>
            <li><a href="ros/ros2_docker.md">ROS2 with Docker</a></li>
            <li><a href="ros/ros2_basics.md">ROS2 basics</a></li>
            <li><a href="ros2_exercises/ros2_asgn.md">Exercise: Test your understanding for ROS2</a> <span style="color: red;">[Required for Bootcamp]</span></li>
            <li><a href="ros/ros-action-server.md">ROS Action Server</a> <span style="color: red;">(ROS1)</span></li>
            <li><a href="ros/reading-sensor-data.md">Reading Sensor Data</a><span style="color: red;">(ROS1)</span></li>
            <li> <a href="game/README.md">ROS and C++ Exercise: AI mechanics for controlling a game</a><span style="color: red;">(ROS1)</span></li>
        </ol>
    </ol>

2. Practical Math Tools in Python for Robotics & System Dynamics
    <blockquote>
    You’ll need a working knowledge of key mathematical tools to implement and debug the algorithms that make robots move, perceive, and plan. The goal of Section 2(A) is not to teach an entire math curriculum, but to equip you with just enough theory — and the right Python libraries — to tackle the coding exercises with confidence. In Section 2(B), we will get into the details of F1Tenth vehicle states & dynamics so that you can implement the algorithms in Section 4. 
    </blockquote>
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

3. Simulation Basics with <code>F1Tenth-Gym-ROS</code>
    <ol type="A">
        <li><a href="https://roboticsknowledgebase.com/wiki/robotics-project-guide/choose-a-sim/">Simulation Basics</a></li>
        <li><code>F1Tenth-Gym-ROS</code></li>
        <ol type="a">
            <li><a href="https://github.com/f1tenth/f1tenth_gym_ros">Setting up the <code>F1Tenth-Gym-ROS</code> environment with ROS2</a></li>
            <li><a href="simulation/exercise1_emergency_braking/README_exercise1_automatic_emergency_braking.md"><code>F1Tenth-Gym-ROS</code> exercise 1: Automatic Emergency Braking</a></li>
            <li><a href="simulation/exercise2_wall_following/README_exercise2_wall_following.md"><code>F1Tenth-Gym-ROS</code> exercise 2: Wall Following</a></li>
            <li><a href="simulation/exercise3_gap_following/README_exercise3_gap_following.md"><code>F1Tenth-Gym-ROS</code> exercise 3: Gap Following</a></li>
        </ol>
        <li>Custom robot and simulation development in Gazebo</li>
        <ol type="a">
            <li> (still in development) </li>
            <li> (still in development) </li>
        </ol>
    </ol>

4. Algorithms
    <blockquote>
    You can use either Python or C++ for these exercises. Python skeleton code is provided in <code>/scripts</code> directory and C++ is provided in <code>/src</code> directory, in each algorithm package.
    </blockquote>

   <ol type="A">
        <li>Mapping algorithms
            <ol type="a">
                <li><a href="algorithms/mapping/README_f1tenth_slam.md">SLAM</a></li>
            </ol>
        </li>
        <li>Localization algorithms
            <ol type="a">
                <li><a href="algorithms/localization/README_f1tenth_amcl.md">Particle Filter: AMCL</a></li>
                <!-- <li>EKF (Extended Kalman Filter) (still in development)</li> -->
            </ol>
        </li>
        <li>Control algorithms
            <ol type="a">
                <li><a href="algorithms/control/README_f1tenth_pure_pursuit.md">Pure Pursuit</a></li>
                <li><a href="algorithms/control/README_f1tenth_mpc.md">MPC (Model Predictive Control)</a></li>
            </ol>
        </li>
        <li>Motion planning algorithms
            <ol type="a">
                <li><a href="algorithms/motion_planning/README_f1tenth_rrt.md">RRT (Rapidly Exploding Tree)</a></li>
                <li><a href="algorithms/motion_planning/README_f1tenth_rrtStar.md">RRT*</a></li>
            </ol>
        </li>
        <li>Reinforcement Learning
            <ol type="a">
                <li>Model-based RL (still in development)</li>
                <li><a href="#rl-car-racing">Model-free RL</a></li>
            </ol>
        </li>
    </ol>

<!-- 5. Integrate and Compare Performance
6. Writing a Technical Report -->


## [RL Car Racing](https://github.com/artrela/RL_Car_Racing/tree/97a08ae8ffca019fe2f20cc5a50658cff0a6548f)
[RL Car Racing](https://github.com/artrela/RL_Car_Racing/tree/97a08ae8ffca019fe2f20cc5a50658cff0a6548f) is an independent course for an introduction to common reinforcement methods (RL) leveraging Gymnasium (formerly OpenAI Gym), developed by Alec Trela. 

## Contributing

If you find a typo or error in the course material, please submit a pull request to the [GitHub repository](https://github.com/roboticsknowledgebase/mrsd-software-bootcamp). If you have a suggestion for a new topic, please open an issue on the repository.
