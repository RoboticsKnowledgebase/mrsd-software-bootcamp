# F1Tenth Exercise 3: Gap Following

> This exercise is based on [CMU 16663 - F1Tenth Course :: Lab 4](https://github.com/f1tenth-cmu/f1tenth_lab4).

> Skeleton code is provided in the [`gap_following_pkg`](/simulation/gap_following_pkg/). Use this package within your ROS2 workspace.

## I. Learning Goals

- Reactive methods for obstacle avoidance

## II. Overview

In this lab, you will implement a reactive algorithm for obstacle avoidance. While the base starter code defines an implementation of the F1TENTH Follow the Gap Algorithm, you are allowed to submit in C++, and encouraged to try different reactive algorithms or a combination of several. In total, the python code for the algorithm is only about 120 lines.

## III. Review of F1TENTH Follow the Gap

The [lecture on F1TENTH "Follow the gap"](https://www.youtube.com/watch?v=5asfD-_Z9x8) (accompanying [lecture slides](https://docs.google.com/presentation/d/11JjzGutwLbgGHyKnrytX-4SCuOkF3Byp78YuN7z4R7Q/edit?usp=sharing) provided by CMU) is the best visual resource for understanding every step of the algorithm. However, the steps are outlined over here:

1. Obtain laser scans and preprocess them.
2. Find the closest point in the LiDAR ranges array.
3. Draw a safety bubble around this closest point and set all points inside this bubble to 0. All other non-zero points are now considered “gaps” or “free space”.
4. Find the max length “gap”, in other words, the largest number of consecutive non-zero elements in your ranges array.
5. Find the best goal point in this gap. Naively, this could be the furthest point away in your gap, but you can probably go faster if you follow the “Better Idea” method as described in lecture.
6. Actuate the car to move towards this goal point by publishing an `AckermannDriveStamped` to the /drive topic.

## IV. Exercise (Implementation)

Implement a gap follow algorithm to make the car drive autonomously around the Levine Hall map. You can implement this node in either C++ or Python. There are two extra test maps `levine_blocked.png`, which is empty, and `levine_obs.png`, which has obstacles that are relatively hard to navigate through for you to evaluate your code on.

To change the map in the simulation, add the included `.png` and `.yaml` map files to `f1tenth_gym_ros/maps` directory. Then, change `f1tenth_gym_ros/config/sim.yaml` to use your desired map.
