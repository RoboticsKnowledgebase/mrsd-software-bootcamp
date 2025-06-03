## Exercise 1: Creating a Package

In this exercise, you'll create a ROS 2 package named `basic_pkg` inside your `basic_ws` workspace running in a **ROS 2 Foxy Docker container**.

### ✅ Step-by-Step Instructions

1. (Optional) Start your container if you're using Docker:

    ```bash
    docker start -ai ros2_foxy_basic
    ```

2. Navigate to your workspace's `src` directory:

    ```bash
    cd /usr/basic_ws/src
    ```

3. Create the package `basic_pkg` with both Python and C++ support and `ackermann_msgs` as a dependency:

    ```bash
    ros2 pkg create basic_pkg \
      --build-type ament_cmake \
      --dependencies rclcpp rclpy ackermann_msgs
    ```

    > 📝 Note: We use `ament_cmake` here to support C++; Python can still be added with a `setup.py` and `ament_python` config if needed.

4. Check your folder structure to make sure it is clean:
    ```bash
    tree /usr/basic_ws -L 2
    ```
    You should **not** see nested `src/`, `build/`, or `install/` directories inside the `src/` folder.

5. Go to the usr of the workspace and install dependencies with `rosdep`:

    ```bash
    cd /usr/basic_ws
    rosdep update --include-eol-distros
    rosdep install -i --from-path src --rosdistro foxy -y
    ```

    When running the second `rosdep`, it is very likely that you will get the following error:
    ```bash
    E: Unable to locate package ros-foxy-ackermann-msgs
    ERROR: the following rosdeps failed to install
        apt: command [sudo -H apt-get install -y ros-foxy-ackermann-msgs] failed
    ```
    This is because `ackermann_msgs` is released as a binary package for ROS2 Humble and newer, but not for ROS2 Foxy. In this case, follow the instructions [below](#in-case-ackermann_msgs-cannot-be-installed-using-rosdep).

6. Build the workspace:

    ```bash
    colcon build
    ```

7. Source the workspace to use your package:

    ```bash
    source install/setup.bash
    ```

You have now created a clean, properly structured ROS 2 package named `basic_pkg` that supports both Python and C++ and depends on `ackermann_msgs`.

## In case `ackermann_msgs` cannot be installed using `rosdep`.

1. Do the following first
    ```bash
    cd ~/basic_ws/src
    git clone https://github.com/ros-drivers/ackermann-msgs.git
    cd ~/basic_ws
    ```
