# F1Tenth Mapping Algorithm: SLAM

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 5](https://github.com/f1tenth-cmu/f1tenth_lab5).

# I. Learning Goals

Here, we introduce SLAM, Simultaneous Localization and Mapping. 

We are not going to implement SLAM ourselves, but instead use `slam_toolbox` to make a map of your surroundings. Please watch [UPenn's F1Tenth lecture on Simultaneous Localization and Mapping (SLAM)](https://www.youtube.com/watch?v=44wwTIJqG_I) and review [CMU's F1Tenth lecture slide on Hector SLAM](https://docs.google.com/presentation/d/1_lT-skCdau-oQQmTk69f0jsdhLGldUUz3WE9q2eSpvg/edit?usp=sharing) (slides are highly recommended). 

# II. SLAM
We won't have you implement SLAM yourselves in this tutorial (that itself can be a whole project). Instead, please use `slam_toolbox` to make a map of the Levine Hall. Then, save the map as `levine_hall.pgm` and `levine_hall.yaml`.

1. Installing `slam_toolbox`
    ```bash
    sudo apt install ros-foxy-slam-toolbox
    ```
2. Before running `slam_toolbox`, make sure the odometry on your vehicle/simulator is tuned!
3. Launcing `slam_toolbox`
    - Launch `teleop` in one window
    - Launch `slam_toolbox` in another window
        ```bash
        ros2 launch slam_toolbox online_async_launch.py params_file:=/home/nvidia/f1tenth_ws/src/f1tenth_system/f1tenth_stack/config/f1tenth_online_async.yaml
        ```
4. Visualization
    - Launch rviz2
    - Add `/map` by topic
    - Add `/graph_visualization` by topic
    - On top left corner of rviz, panels > add new panel > add `SlamToolBoxPlugin` panel
    - Once you're done mapping, save the map using the plugin. You can give it a name in the text box next to "Save Map". Map will be saved in whichever directory you ran `slam_toolbox`.

