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

# III. Logging Waypoints

There are several methods you can use to create waypoints for a specific map.

1. Recording a trajectory of joystick driven path. You can write a node that subscribe to the pose provided by the particle filter localization, and save the waypoints to a csv file. A similar script is provided [here](https://github.com/f1tenth/f1tenth_labs/blob/main/waypoint_logger/scripts/waypoint_logger.py). Note that this script is in ROS 1 and you'll have to write a ROS 2 node.

2. Find key points in the map (e.g. in the AI makerspace corridor, the turning points at the gym lockers) and create a interpolated spline that goes through all the corners. You can use functions such as `scipy.interpolate.splprep` and `scipy.interpolate.splev`. You can find more documentaion on these [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html) and [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev).

Usually, you'll just save the waypoints as `.csv` files with columns such as `[x, y, theta, velocity, arc_length, curvature]`. With pure pursuit, the bare minimum is `[x, y]` positions of the waypoints. Another trick is that you can also smooth the waypoints if you decided to record it with the car. You can subsample the points you gathered and re-interpolate them with the `scipy` functions mentioned above to find better waypoints.

# IV. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).
