#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
import pygame

def keyboard_to_joy():
    pygame.init()
    pygame.display.set_mode((100, 100))  # Dummy window needed for pygame events

    rospy.init_node('keyboard_to_joy_publisher', anonymous=True)
    pub = rospy.Publisher('/joy', Joy, queue_size=10)
    rate = rospy.Rate(10)  # Adjust the rate as needed

    while not rospy.is_shutdown():
        pygame.event.pump()  # Process pygame events

        # Create Joy message
        joy_msg = Joy()
        joy_msg.header.stamp = rospy.Time.now()

        # Read keyboard inputs
        keys = pygame.key.get_pressed()
        joy_msg.axes = [0.0] * 6  # 6 axes
        joy_msg.buttons = [0] * 12  # 12 buttons

        # Map arrow keys to Joy message
        if keys[pygame.K_UP]:
            joy_msg.axes[1] = -1.0  # Move forward
        elif keys[pygame.K_DOWN]:
            joy_msg.axes[1] = 1.0  # Move backward

        if keys[pygame.K_LEFT]:
            joy_msg.axes[0] = -1.0  # Move left
        elif keys[pygame.K_RIGHT]:
            joy_msg.axes[0] = 1.0  # Move right

        # Publish Joy message
        pub.publish(joy_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        keyboard_to_joy()
    except rospy.ROSInterruptException:
        pass
