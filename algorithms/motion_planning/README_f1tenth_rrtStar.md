# F1Tenth Motion Planning Algorithm: RRT*

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 6](https://github.com/f1tenth-cmu/f1tenth_lab6).

> Skeleton code is provided in the [`rrt_pkg`](/algorithms/motion_planning/rrt_pkg/). Use this package within your ROS2 workspace.

# I. Learning Goals

Much of the learning goals in this exercise are the same as those in [RRT exercise](/algorithms/motion_planning/README_f1tenth_rrt.md#i-learning-goals). On top of that, we urge you to push yourself and implement your own version of RRT*.

# II. Overview
In the paper [Sampling-based Algorithms for Optimal Motion Planning by Karaman, et al.](https://arxiv.org/pdf/1105.1186.pdf), pay close attention to Algorithm 6, as shown below.

### RRT* Pseudocode
![](/algorithms/fig/rrtStar_algo.png)

This is the pseudocode of RRT*. You can find  details of the functions used by RRT* in the paper.


# III. Implementation

On top of the basic version of RRT, RRT* uses a cost function, and rewiring the tree, to find a better path to the goal. When the tree has expanded infinite number of nodes, RRT*'s solution is close to optimal. The figure below shows the difference in the tree expanded and path found between RRT and RRT*. The skeleton code in [`rrt_pkg`](/algorithms/motion_planning/rrt_pkg/) provided has sections for functions in RRT* as well.

![](/algorithms/fig/rrt_vs_rrtStar.png)