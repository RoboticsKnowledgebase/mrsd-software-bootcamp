# Programming Familiarization Part 1

## Goal

1. To give you practical experience in writing and debugging actual C++ applications and give you more practice at memory in C++.
2. To familiarize with using ROS and OpenGL tools with C++/Python

## Part 1. Practice Problems (15%)

Given the following structs, answer question 1. You may assume that all pointers are initialized
and are valid.

```cpp
struct A {
    float data;
};

struct B {
    A a;    
};

struct C {
    B* b;
};

struct D {
    C c;
};
```

1. Given a pointer to struct D called “d”, what expression will access “data”, the member of struct A?
2. Given the following structs, predict the memory layout of a struct A named “stack”. You may assume that it is a 32-bit machine.

```cpp
struct A{
    float a, b, c;
    B* ptr;
    B mem;
};

struct B {
    float d, e;
};

A stack;
```


| Address | Expressions
| --- | --- |
| A+0x0 | stack, stack.a |
| A+0x | |
| A+0x | | 
| A+0xC | |
| A+0x | |
| A+0x | |

3. Given the functions below, what is the value stored  in the points a and b after calling foo?

```cpp
struct point {
    float x, y;
};

void foo(point& p1, point p2) {
    point p3;
    p3.x = p1.x + p2.x;
    p3.y = p1.y + p2.y;
    bar(p3);
    p1.x -= p3.x;
    p1.y -= p3.y;
}

void bar(point p3) {
    p3.x *= .5f;
    p3.y *= .5f;
}

point a, b;
a.x = b.y = 1;
a.y = b.x = 0;
foo(a, b);
```


## Part 2. Coding Problem (85%)

This portion of the assignment assumes you have some experience in coding C++ and be able to use ROS and OpenGL. If you do not, it might be a bit of a challenge and you should start early.

You will code an AI that will try to survive the longest in a barrage of virtual missiles. This assignment will walk you through the basics of building a very simple AI that will do well in simple scenarios (1 - 2 projectiles in the air).

### Part 2.1. Setup

This software can be run on any OS, but I will only detail installation for Ubuntu. Install CMake, build-essentials, X11 libraries, and OpenGL using the commands 

```
sudo apt-get install cmake build-essential xorg-dev libgl1-mesa-dev mesa-utils.
```

1. In order to build the program, you will need a C++11-compliant compiler; if you are using Ubuntu 16.04, you should have at least gcc-5.4, but you can check the version using gcc -v. 

2. Next, clone this repository 

```
git clone https://github.com/RoboticsKnowledgebase/mrsd-software-bootcamp.git
```

3. This repository contains subdirectories src, include, shaders, etc. and can be compiled with using ROS catkin_make. For this first create a new workspace with (this is assuming you have Ubuntu 20.04 and thus ROS Noetic. replace noetic with the version you have installed) :-

```
source /opt/ros/noetic/setup.bash
mkdir -p ~/game_ws/src
cd ~/game_ws/
catkin_make
```

4. Now copy the game package associated with this repo to your workspace

```
cp -r <path-to-cloned-repo>/game ~/game_ws/src/ 
```

5. Install all dependencies associated with the package with (if you do not have rosdep installed, install it with 'sudo apt-get install python3-rosdep'):-

```
cd ~/game_ws
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

6. Build the workspace with :-

```
catkin_make
```

7. Open a new terminal and run roscore in it

```
source /opt/ros/noetic/setup.bash
roscore
```

8. Go back to first terminal, source the workspace and launch the game with :-

```
source devel/setup.bash
rosrun game missildedefense
```

This will open a new window with the game running. Controls: Press ‘C’ to spawn an AI controller player. Press ‘Space’ to spawn a user-controlled player. Use the left and right arrow keys to move your player. Pressing 'C' will spawn the agent that will listen to /joy topic and move according to it

9. (Optional) if you have a joystick, connect it and use the left axis to control the player. If you do not have a joystich, run keyboard_to_joy.py which listens to arrow keys on keyboard to publish to /joy topic :-

```
cd ~/game_ws/src
python3 keyboard_to_joy.py
```

This will open a new window, keep that window active and use arrow keys to control the player. If you do no have pygame install, install it with 'pip install pygame'

10. You will get the game state and game image as ROS topics that you can read through a new AI node that you will write and publish to /joy topic to control the player. To see the active topics run :-

```
source /opt/ros/noetic/setup.bash
source ~/game_ws/devel/setup.bash
rostopic echo
```

And you should see '/game_state', '/game_image' and '/joy' topics. Check the messages in '/game_state' with :-

```
rostopic echo /game_state
```

You can see the enemy, player, projectile, explosions positions, and other game info which is useful in determining where the player should go to avoid being hit by projectiles. You can also see the game image, for that open rviz with 'rviz' command in new terminal (Make sure to source ROS noetic and your workspace). In rviz, add '/game_image' topic to see the game image. Your task is to subsribe to these topics and command the player to avoid getting hit.


### Part 2.2. Game Mechanics

Now it is time to dive into some code and understand the exact mechanics behind the game. **You don’t have to write up answers for any questions asked in this section.** This is just an overview of the mechanics and a guide on diving into the details of the mechanics.

As you can guess, the goal of the game is to have your character survive as long as possible. Your character is denoted by the blue circle at the bottom of the window. There are enemies on the map, denoted by the large red circles, which shoot projectiles out of them in an
attempt to hit you. These projectiles are yellow and act as simple Newtonian objects under gravity. When the projectiles hit the ground they generate a fixed-size explosion that is dangerous for any player to touch and will result in the player losing the game. The only method by which your player can avoid projectiles is by moving horizontally along the ground.

To dive deeper into the mechanics of the game, we are going to explore some of the game code to get a better idea of what’s going on. Take a look at `Game.cpp`, specifically the function tick. This is where all the game update logic occurs.

1. If you are not familiar with the structures used in the loops that are in the function, take a look at this [tutorial](http://www.cprogramming.com/tutorial/stl/iterators.html) and peruse the documentation for [vectors](http://en.cppreference.com/w/cpp/container/vector) and [lists](http://en.cppreference.com/w/cpp/container/list).
2. Think about what types the iterator is being dereferenced (“*”) to.
3. Next, examine the `tickProjectile` function.
    1. What is the purpose of the function?
    2. Why is the Projectile passed with a &? (And what does the & mean? See [this](http://www.learncpp.com/cpp-tutorial/73-passing-arguments-by-reference/))
    3. Do the updated equations for position and velocity make sense to you?

Feel free to take a similar tour of the remaining functions in `Game` to familiarize yourself with the game logic. Also, take particular note of the order in which things like “explosion checks” are done and when explosions take effect.


### Part 2.3 AI Mechanics

#### Part 1

The AI that you are going to write is going to be pretty simple. You will be given the whole state of the game (enemies, players, projectiles, and explosions) and you will try to stay alive. For this you are free to write a node in either python and c++ that reads game_state and determines a strategy to move the player to stay safe. 

The most crucial aspect of building this AI is predicting when spots on the ground will be unsafe (due to explosions). Therefore, we need to know where and when projectiles are going to hit the ground. You can first built a function in the controller node that returns both a time and a position for the point of impact. To do this it can use constants taken from the '/game_state' topic.

The next task will be to actually determine which spots are going to be safe and when. For this you can have `determineSafeSpots` method in your controller node that uses the results from `trackProjectile` to determine which spots on the ground are going to be safe. 

*HINT* if you inspect the game you will discover that the way the game checks if a certain “spot” is unsafe is by dividing the game space into W cells. When projectiles explode, cells are marked unsafe, and when they disappear, they are marked safe again. It stands to reason that when you are determining when spots are safe/unsafe you might use a similar discretization approach. The function prototype is also up to you and the method of storing information is up to you.

The next function to implement is `pickSafeSpot`. Depending on how you would like to implement the AI, this may or may not be entirely useful, but I found it useful in testing my last two helper functions. Just like it says, `pickSafeSpot` just picks a spot from the determined spots and returns that.

After all this, you are requored to command '/joy' to move the player either left or right. A common strategy would be to determine safe spots, pick one, and move your player towards that. Create a new node named 'controller_full_state' for this task

#### Part 2

After implementing the strategy by reading the full game state info, your next task is to accomplish the same task but by just reading the game image and not using the '/game_state' topic to read the complete game state. This would be the exact same setting as a human would observe from the game and react to it. For this you will need to use OpenGL or OpenCV library to read the image from '/game_image' topic, extract the enemy, projectile, player and explosion positions and control player accordingly instead of directly using them from '/game_state'. Create a separate node named 'controller_image' for this task 

### Self assessment

Your AI should be able to predict and avoid projectiles in the “Medium” Scenario and survive for at least 1 minute. (Keep in mind this is randomized so the expectation is that your AI will survive longer than 1 minute and that it’s not just luck). Your AI is not required to survive in difficulties Hard and above; these scenarios are available for you to test and try out. 


The scenario can be adjusted within the startup.cpp file by changing which “setup” function is used in the main function or by simply passing an additional <difficulty> argument when running './missiledefense <difficulty level>'.

Once you are done testing, you can run autograder by running 'autograder/run_autograder.sh' as:-

```
cd autograder/
bash run_autograder.sh
```
