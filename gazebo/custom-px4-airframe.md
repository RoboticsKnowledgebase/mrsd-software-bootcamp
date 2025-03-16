# What is PX4
[PX4](https://px4.io/) is an open-source flight control software for drones and unmanned vehicles. It provides a powerful and flexible platform for real-time flight control, sensor fusion, and mission planning. PX4 is designed to support a wide variety of airframes, including multirotors, fixed-wing aircraft, and VTOL systems.

Key features of PX4 include:
- **Real-time Flight Control:** Achieve precise, stable control of your aircraft under various conditions.  
- **Extensible Architecture:** Easily integrate additional sensors, actuators, or custom algorithms.  
- **Open-Source Community:** Contribute to and benefit from active development and community support.  
- **Compatibility:** Seamlessly work with ground control stations like [QGroundControl](https://qgroundcontrol.com/) and simulators such as [Gazebo](https://gazebosim.org/).  

Now, you can use PX4 to achieve manual control of drones or ground vehicles, i.e., using radio transmitter controllers or joysticks. But, its real power is in the seamless integration with autonomous control stacks and various robotics softwares and programming languages. For example, it provides a nice integration with [MAVROS](https://wiki.ros.org/mavros) so that you can directly communicate with your PX4-based drone using ROS. 

Furthermore, it provides great integration with simulations such as Gazebo. This way, you can test your whole software stack in Gazebo even before deploying your autonomy stack in the wild. Using ROS, you can communicate with your virtual drone in Gazebo.

# PX4 in Gazebo Classic Simulation
**NOTE!** In this tutorial we are using [Gazebo Classic Simulation](https://docs.px4.io/main/en/sim_gazebo_classic/) (EOL in 2025). Gazebo Classic is best served in macOS, Ubuntu 18.04, 20.04, and WSL2 while using ROS. If you want to use [Gazebo](https://gazebosim.org/home) (previously Gazebo Ignition, aka the new Gazebo), please use Ubuntu 22.04 and ROS2. The appropriate tutorial for adding a new airframe in PX4 using Gazebo (Ignition) is provided in [PX4 User Guide](https://docs.px4.io/v1.12/en/dev_airframes/adding_a_new_frame.html).