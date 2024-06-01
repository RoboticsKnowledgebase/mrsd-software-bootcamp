#!/usr/bin/env python3

import rclpy
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.node import Node
from std_msgs.msg import String 
from rcl_interfaces.msg import SetParametersResult
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped
from os.path import expanduser
from time import strftime, gmtime

# home = expanduser('~')
file_path = '/sim_ws/logs/' + strftime('%Y-%m-%d-%H-%M-%S',gmtime()) +'.csv'
file = open(file_path,'w')

class WayPtLogger(Node):
    def log_callback(self, inferred_pose):
        print('Inside callback')
        file.write('%f, %f, %f, %f, %f, %f, %f\n' %(inferred_pose.pose.pose.position.x, inferred_pose.pose.pose.position.y, inferred_pose.pose.pose.position.z, inferred_pose.pose.pose.orientation.x, inferred_pose.pose.pose.orientation.y, inferred_pose.pose.pose.orientation.z, inferred_pose.pose.pose.orientation.w)) 


    def __init__(self):
        super().__init__('waypoint_logger')
        self.odom_subs = self.create_subscription(Odometry, 'ego_racecar/odom', self.log_callback, 10)
        # self.odom_subs = self.create_subscription(Odometry, '/pf/viz/inferred_pose', log_callback, 10)
        print('Initialized WayPointLogger')


def main(args=None):
    rclpy.init(args=args)
    waypoint_logger = WayPtLogger()
    rclpy.spin(waypoint_logger)
    waypoint_logger.destroy_node()
    file.close()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
