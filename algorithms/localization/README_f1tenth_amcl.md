# F1Tenth Localization Algorithm: Particle Filter

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 5](https://github.com/f1tenth-cmu/f1tenth_lab5).

# I. Learning Goals

Here, we are getting into localization, specifically, we are going to learn about and use particle filter. 

Please watch [UPenn's F1Tenth lecture on Localization using Particle Filters](https://www.youtube.com/watch?v=l_nWiL3mkzQ) and review [CMU's F1Tenth lecture slide on Particle Filters](https://docs.google.com/presentation/d/1_lT-skCdau-oQQmTk69f0jsdhLGldUUz3WE9q2eSpvg/edit?slide=id.g32d2797e3b8_0_201#slide=id.g32d2797e3b8_0_201) and [Particle Filter Analysis](https://docs.google.com/presentation/d/1lhAccUMHzO9wLGNV27DEGQC8e7IxV1d2LUMXWq6FUp0/edit?slide=id.g281a8cfd964_1_234#slide=id.g281a8cfd964_1_234).

# II. Particle Filter

Once you have a comprehensive understanding of localization with particle filters, run `particle_filter` on the car using the map you made with SLAM inside the simulator.

1. Clone the `range_libc` repo:
    ```bash
    git clone https://github.com/f1tenth/range_libc.git
    ```
2. Install with the following commands:
    ```bash
    cd range_libc/pywrapper
    ```
    ```bash
    sudo WITH_CUDA=ON python setup.py install
    ```
3. Clone the `particle_filter` package
    ```bash
    cd /home/{username}/{workspace}/src
    ```
    ```bash
    git clone https://github.com/f1tenth/particle_filter.git
    ```
4. Install dependencies
    ```bash
    rosdep install -r --from-paths src --ignore-src --rosdistro foxy -y
    ```
5. Compile your workspace again and source it
    ```bash
    cd /home/{username}/{workspace} && colcon build
    ```
    ```bash
    source install/setup.bash
    ```
6. Launching `particle_filter`
    - Launch `teleop` in one window
    - Launch `particle_filter` in another window
        ```bash
        ros2 launch particle_filter localize_launch.py
        ```
7. Visualization
    - Launch rviz2
    - Add `/map` by topic
    - In the settings for `/map`, change durability policy under topic to `transient local`.
    - To show the current localization, add `/pf/viz/inferred_pose` topic.
    - Optionally, you can add `/pf/viz/particles` to see the particles.
8. Check the update frequency
    Check the publishing frequency on `/pf/viz/inferred_pose`. It should be at least 30 Hz.
9. Changing the map in use
    - Put the map files (`.png` image and `.yaml` file) in `particle_filter/maps`.
    - Change `particle_filter/config/localize.yaml` to reflect the map you want to use.
10. Use the "2D Pose Estimate" to set the initial position for the particle filter, as shown below in the figure:
![](/algorithms/fig/particle_filter_instruction.png)