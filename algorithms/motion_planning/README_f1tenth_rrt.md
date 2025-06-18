# F1Tenth Motion Planning Algorithm: RRT

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 6](https://github.com/f1tenth-cmu/f1tenth_lab6).

> Skeleton code is provided in the [`rrt_pkg`](/algorithms/motion_planning/rrt_pkg/). Use this package within your ROS2 workspace.

# I. Learning Goals

- Motion planning basic concepts
    - **Configuration space vs Workspace**: you should understand the difference between configuration space and workspace, and the advantages and disadvantages of planning in each of them.
    - **Free space vs Obstacle space**: you should understand the difference between free space and obstacle space.
    - **Occupancy grids and Costmaps**: you should understand what occupancy grids and costmaps are, how to use them, and how to create them.
- Motion planning algorithms
    - **Sampling based algorithms**: RRT (Rapidly Exploding Tree) and its variants.

# II. Overview
After finishing this lab, and successfully implementing RRT, your car should be able to do something like [this](https://www.youtube.com/watch?v=llHCRqwIllM). 

Before you start this lab, you should read the paper [Sampling-based Algorithms for Optimal Motion Planning by Karaman, et al.](https://arxiv.org/pdf/1105.1186.pdf) Pay close attention to Sections 3.1, 3.2, and 3.3. For the RRT algorithm, refer to Algorithm 3, as shown below.

### RRT Pseudocode
![](/algorithms/fig/rrt_algo.png)

This is the pseudocode of the vanilla RRT. You can find all the details of the functions used by RRT in the paper. For [RRT*](/algorithms/motion_planning/README_f1tenth_rrtStar.md), or another version of RRT, read the RRT* section of the provided paper and Algorithm 6. 

### F1Tenth RRT vs Generic RRT
In general, RRT is often used as a global planner where the tree is kept throughout the time steps. Whenever there is a new obstacle, and the occupancy grid changes, the tree will change accordingly. In our case, RRT is used as a local planner for obstacle avoidance. This is due to the fact that we don't have a well-defined starting point and goal point when we're racing on a track and we want to run continuous laps. In our implementation, we are only keeping a tree for the current time step in an area around the car. You could try to keep one tree that populates the map throughout the time steps, but speed is going to be an issue if you don't optimize how you're finding nodes, and traversing the tree.

# III. Implementation
You can choose to implement RRT in either the workspace or configuration space. Since we're working with a car-like robot, the workspace will be the car's position in the world, and the configuration space will be whatever you decided to add on top of that (heading angle, velocity, etc.).

### Implementing an Occupancy Grid
You'll need to implement an occupancy grid for collision checking. Think about what is available to you (the map, the Laserscan messages, etc.), and construct a occupancy grid using those information. You can choose to either implement a binary occupancy grid (a grid cell is either 0 for unoccupied, or 1 for occupied), or use a probabilistic occupancy grid (a grid cell has values between 0 and 1 for probability that it is occupied). You could choose to implement either an occupancy grid in the car's local frame (our recommendation), or in the map's global frame. Depending on the size of the map that you use, think about how to compute updates to the occupancy grid and storing/using the occupancy grid efficiently. Since we're using RRT as a local planner, as in it comes up with a new path at every time step, you need to run everything relatively fast. You'll also want to visualize the occupancy grid to ensure its correctness. You don't have to implement a multi-layer one like the one shown in the figure below.

![](/algorithms/fig/grid.png)

### Working in the simulator
By this point, you should be pretty comfortable using the simulator to test your code. The ground truth pose of the car is available in the simulator, this would be useful for testing your algorithm in the simulator. 

### Trajectory Execution
After you've found a path to your goal with RRT, there are different algorithms that you could use to follow that trajectory. The most obvious solution is Pure Pursuit that you have done from the last lab. Picking the waypoint out of the path for pure pursuit will be the most important part if you decided to go down this route. You want a balance between having the car steering smoothly, and at the same time, reactive enough to avoid obstacles. Also, up-sampling the path for pure pursuit to pick out a waypoint is a good way to go.

### Hints
Think about how you could change the way that you're sampling the free space to speed up the process of finding a path to the goal. Also think about how the restrict the area in which you're sampling to make sure you don't have too big of a tree. Besides RRT*, there are other versions of RRT that takes into consideration of other variables (the dynamics of the car for example). After you're done with the basic version of RRT, you should do some research and implement a better version of RRT.

Make sure you visualize the tree you've expanded, and the path you've chosen as the trajectory.