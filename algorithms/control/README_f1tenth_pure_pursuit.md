# F1Tenth Control Algorithm: Pure Pursuit

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 5](https://github.com/f1tenth-cmu/f1tenth_lab5).

> Skeleton code is provided in the [`pure_pursuit_pkg`](/algorithms/control/pure_pursuit_pkg/). Use this package within your ROS2 workspace.

# I. Learning Goals

Here, we introduce Pure Pursuit. The core idea is that a reference point can be placed on the path at a fixed distance ahead of the vehicle, and the steering commands needed to intersect with this point using a contant steering angle can be computed. As the vehicle turns towards the path to follow this curve, the point continues to move forward, reduing the steering angle and gently bringing the vehicle towards the path. Please watch [UPenn's F1Tenth lecture on Pure Pursuit](https://www.youtube.com/watch?v=x9s8J4ucgO0) and review [CMU's F1Tenth lecture slide on Pure Pursuit](https://docs.google.com/presentation/d/1RraOGf4eY9SquIqnXgv0p7Q9DL8AgPmP6eYs_lKtNcc/edit?usp=sharing). Furthermore, you can refer to [R. Raig Coulter's paper, *"Implementation of the Pure Pursuit Path Tracking Algorithm"*](https://www.ri.cmu.edu/pub_files/pub3/coulter_r_craig_1992_1/coulter_r_craig_1992_1.pdf).
![](/algorithms/fig/PurePursuit.png)

# II. Preliminaries

The control algorithm, such as Pure Pursuit, is the last stage in our system. The system overview is as follows, and the preliminary requirements for Pure Pursuit to work adhere to them:

1. **Mapping**: The vehicle needs a map of the world first. To achieve this, please review [Mapping Algorithm - SLAM](/algorithms/mapping/README_f1tenth_slam.md) to run `slam_toolbox`.

1. **Localization**: Once the vehicle has a map of the world, we need it to be smart enough to perceive the surroundings and localize within this track. Please review [Localization Algorithm - AMCL](/algorithms/localization/README_f1tenth_amcl.md) to run `particle_filter`.

1. **Path Planning**: Now, the vehicle knows where it is relative to the world. It needs to also know where to move. There are several ways to achieve this, such as making an optimal raceline using optimization techniques (for more information about this, please review [CMU's F1Tenth lecture on Raceline Optimization](https://docs.google.com/presentation/d/1vHV9529lP9Ask9SOXVhYKz2ZJR7zCD5OY_Sysyvy1AI/edit?usp=sharing)). Here, we will simply log the desired waypoints. Please follow the [next section](#iii-logging-waypoints).

1. **Control**: The vehicle now knows where it is and where to move. We will control the vehicle using [Pure Pursuit](#v-pure-pursuit-implementation).

# III. Logging Waypoints

There are several methods you can use to create waypoints for a specific map.

1. Recording a trajectory of joystick driven path. You can write a node that subscribe to the pose provided by the particle filter localization, and save the waypoints to a csv file. A similar script is provided [here](https://github.com/f1tenth/f1tenth_labs/blob/main/waypoint_logger/scripts/waypoint_logger.py). Note that this script is in ROS 1 and you'll have to write a ROS 2 node.

2. Find key points in the map (e.g. in the AI makerspace corridor, the turning points at the gym lockers) and create a interpolated spline that goes through all the corners. You can use functions such as `scipy.interpolate.splprep` and `scipy.interpolate.splev`. You can find more documentaion on these [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html) and [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev).

Usually, you'll just save the waypoints as `.csv` files with columns such as `[x, y, theta, velocity, arc_length, curvature]`. With pure pursuit, the bare minimum is `[x, y]` positions of the waypoints. Another trick is that you can also smooth the waypoints if you decided to record it with the car. You can subsample the points you gathered and re-interpolate them with the `scipy` functions mentioned above to find better waypoints.

# IV. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

# V. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node in the [`pure_pursuit_pkg`](/algorithms/control/pure_pursuit_pkg/). When you're testing in the simulator for the first time, use the groud truth pose provided by the sim as the localization. Then, use particle filter to provide localization.

As shown in the lecture, the curvature of the arc to track
can be calculated as:

<!-- ![](https://latex.codecogs.com/svg.latex?\gamma=\frac{2|y|}{L^2}) -->
$$\gamma=\frac{2|y|}{L^2}$$

1. Make the map files `.pgm` and `.yaml` that you've made using `slam_toolbox`. These could be provided in the `F1Tenth-Gym-ROS` simulator.

1. Implement the Pure Pursuit algorithm using mapping and localization algorithms.

1. Show that Pure Pursuit algorithm controls the vehicle to follow your waypoints.