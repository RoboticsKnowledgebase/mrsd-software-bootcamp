# F1Tenth

## I. Learning Goals

Goal of this tutorial is to get familiarized with full stack deployment using ROS2. We are going to use F1Tenth simulator platform. The aim of this tutorial is to familiarize with how different processes in a stack interact with each other. In this bootcamp, you are going to learn the following:- 
- Installing and using F1Tenth simulator
- Localization with Particle Filter
- Waypoint marking (global planner)
- (optional) RRT local planner  
- Pure Pursuit controller

Much of this exercise is thanks to [UPenn's F1Tenth course](https://roboracer.ai/).


## II. Installing F1Tenth simulator

We will be using F1Tenth simulator for this workshop. Navigate to [f1tenth_gym_ros](f1tenth_gym_ros/README.md) for instructions on how to install and get started with using F1Tenth simulator

## III. Localization on the simulator

Simulator comes with an inbuilt localization.  You can read the car's position relative to the map under /tf or /pose topics. 

## IV. Logging Waypoints

There are several methods you can use to create waypoints for a specific map.

1. Recording a trajectory of joystick driven path. You can write a node that subscribe to the pose provided by the particle filter localization, and save the waypoints to a csv file. A similar script is provided [here](https://github.com/f1tenth/f1tenth_labs/blob/main/waypoint_logger/scripts/waypoint_logger.py). Note that this script is in ROS 1 and you'll have to write a ROS 2 node.

2. Find key points in the map (e.g. in the AI makerspace corridor, the turning points at th gym lockers) and create a interpolated spline that goes through all the corners. You can use functions such as `scipy.interpolate.splprep` and `scipy.interpolate.splev`. You can find more documentaion on these [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splprep.html) and [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.splev.html#scipy.interpolate.splev).

Usually, you'll just save the waypoints as `.csv` files with columns such as `[x, y, theta, velocity, arc_length, curvature]`. With pure pursuit, the bare minimum is `[x, y]` positions of the waypoints. Another trick is that you can also smooth the waypoints if you decided to record it with the car. You can subsample the points you gathered and re-interpolate them with the `scipy` functions mentioned above to find better waypoints.

## V. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## VI. (optional) RRT local planner

Go to [rrt](rrt/README.md) for instructions to implement rrt local planner for obstacles avoidance. This part is optional if you are using levine_blocked map which has obstacles

## VII. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node under pure_pursuit directory. Fill either scripts/pure_pursuit.py or src/pure_pursuit.cpp to run the pure pursuit controller to track global plan from marked waypoints or local plan from RRT planner

## VIII. Putting everything together

Once you have implemented everything, run the f1tenth sim, RRT local planner (optional for obstacle avoidance) and your pure pursuit controller. Pure pursuit controller node should communicate with sim to get the localized position, RRT local planner to get local path (or use the waypoint path directly if not implemented) and should publish the commands to /drive topic to drive the car around the map on the marked trajectory while avoiding obstacles 

# IX. Solution

As this is a self-asessment tutorial, the solution for waypoint logging, pure pursuit controller and rrt planner are given under Solution folder. The videos of the runs are in Solution/videos.md for you to check how the run should look like on the simulator. To re-iterate, the purpose of this tutorial is to familiarize you with the basics of ROS2 and how nodes communicate with each other on ROS2, implementation of full navigation stack with basic algorithms like Pure pursuit, RRT
