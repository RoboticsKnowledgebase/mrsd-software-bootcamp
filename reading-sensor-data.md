# Reading Sensor Data

A key part of writing software for robotics is reading sensor data. This article will go over the basics of reading sensor data in ROS.

## Introduction to Sensor interfaces

A device driver is a program that controls a particular type of device that is attached to your computer. There are device drivers for printers, displays, external disks, and so on. When you buy an operating system, many device drivers are built into the product. However, if you later buy a new type of device that the operating system didn't anticipate, you'll have to install the new device driver. A device driver essentially converts the more general input/output instructions of the operating system to messages that the device type can understand.

The Linux kernel includes a number of device drivers in the kernel itself, but also supports a wide range of modular device drivers that can be loaded separately from the kernel itself. This allows the kernel to be extended with support for new hardware as it becomes available, without needing to recompile the kernel or reboot the system. This also allows users to experiment with new device drivers without affecting the stability of the system.

## Difference between a sensor driver and a program that reads sensor data

A program that reads sensor datais different from a sensor driver in that it does not control the sensor - simply reads data coming from the sensor and then processes the data in some way. For example, a program that reads data from a web cam might display the data on the screen or save it to a file. But this is different from a camera driver, which controls the camera itself and various settings related to the capture.

## Sensor data in ROS

A ROS node is a program that performs some computation. A node can be written in any supported language, including C++, Python, and Java. A node can also be written in a combination of languages, such as C++ and Python.

A common paradigm in working with sensor data in ROS is using a dedicated sensor reader node that reads data from a sensor and then publishes to a topic. Other nodes requiring sensor data can then subscribe to the topic and receive the data.

This is a very flexible way to read sensor data, because it allows you to easily add new nodes that process the data in different ways. This is also a very scalable way to read sensor data, because you can add as many nodes as you want to process the data in different ways. Another benefit of this paradigm is that there is a good separation between hardware integration and computational logic - the sensor reader node is responsible for reading data from the sensor, while the other nodes are responsible for processing the data to achieve the goal of the system.

In this design, the different ROS nodes can be written in different languages. For example, the sensor reader node might be written in C++, while the other nodes might be written in Python.

## Reading sensor data in ROS

The below example shows how to read weight data from a weighing scale connected over serial cable in ROS using a dedicated sensor reader node that reads data from a sensor and then publishes to a topic `/weighing_scale`. Other nodes requiring sensor data can then subscribe to this topic and receive the data.

The script is followed by the msg file that defines the message type `Weight` published over the topic.

`read_weight.py`
```python
#!/usr/bin/env python

import re
import rospy
import serial

from sensor_interface.msg import Weight

# define a function to read data from the sensor
# do not hardcode the device name, instead read it from the parameter server
def read_weight(device="/dev/ttyUSB0", publish_rate=20):
    pub = rospy.Publisher("weighing_scale", Weight, queue_size=10)
    count = 0
    rospy.init_node("weighing_scale")
    rate = rospy.Rate(publish_rate)
    ser = serial.Serial(device, 9600, timeout=1)

    # publish data continuously
    while not rospy.is_shutdown():

        # read and parse data from sensor (in this case via serial port)
        line = ser.readline()  # read a '\n' terminated line
        if type(line) is bytes:
            data = line.decode("utf-8")
            parsed_data = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", data)
            if len(parsed_data) == 0:
                rospy.logerr(
                    f"Invalid value from sensor. Raw value received: {data}"\
                    + "Likely causes include exceeding weighing scale range."
                )
                continue

            # populate message fields and publish
            send_msg = Weight()
            send_msg.header.seq = count
            send_msg.header.stamp = rospy.Time.now()
            send_msg.weight = float(parsed_data[0])
            if data[0] == '-':
                send_msg.weight *= -1
            count += 1
            pub.publish(send_msg)
            rate.sleep()
        else:
            rospy.logwarn("Garbage value recieved from the weighing scale")


if __name__ == "__main__":
    try:
        # read device name from parameter server and start reading data
        read_weight(device=rospy.get_param('device'))
    # handle exceptions gracefully, in this case shutdown ros cleanly
    except rospy.ROSInterruptException:
        pass
```

`Weight.msg`

```bash
cd ~/ros_ws/src/sensor_reader
mkdir msg
touch msg/Weight.msg
```

