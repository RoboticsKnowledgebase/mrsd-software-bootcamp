#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math

import numpy as np
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter
from nav_msgs.msg import Odometry
import  geometry_msgs
from visualization_msgs.msg import Marker, MarkerArray
import csv

# csv file stored here
file_path = '/sim_ws/logs/csv_sim.csv' 
file = None

# Read data from the csv file row by row
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def find_distance(point1, point2):
    return math.sqrt(((point2[0] - point1[0])**2) + ((point2[1] - point1[1])**2))

class PurePursuit(Node):
    """ 
    Implement Pure Pursuit on the car
    This is just a template, you are free to implement your own node!
    """
    def __init__(self):
        super().__init__('pure_pursuit_node')
        drive_topic = '/drive'
        odometry_topic = '/ego_racecar/odom'
        marker_topic = '/visualization_array'

        self.declare_parameter('speed')
        self.declare_parameter('steering_angle')
        
        # Publish steering angle to drive and subscribe to odom topic to get the ground
        # truth pose
        self.drive_ = self.create_publisher(AckermannDriveStamped, drive_topic, 10)
        self.subscriber_odom = self.create_subscription(Odometry, odometry_topic, self.pose_callback, 10)
        self.marker = self.create_publisher(MarkerArray, marker_topic, 10)
        
        # Read data from the csv file
        self.csv_data = read_csv_file(file_path)

        # Publish the marker array
        self.publish_markers(self.csv_data)

    # Function to publish the marker array
    def publish_markers(self, array):      
        marker_array = MarkerArray()
        num = 0
        
        for i in range(len(array)):
            message = array[i]

            marker = Marker()
            marker.header.frame_id = "map"
            marker.header.stamp = self.get_clock().now().to_msg()
            marker.id = i
            self.get_logger().info('x: %f, y: %f, z: %f, ox: %f, oy: %f, oz: %f, oz: %f'  % (float(message[0]), float(message[1]), float(message[2]), float(message[3]), float(message[4]), float(message[5]), float(message[6])))
            # marker.type = Marker.POINTS
            marker.action = Marker.ADD
            marker.pose.position.x = float(message[0])
            marker.pose.position.y = float(message[1])
            marker.pose.position.z = float(message[2])
            marker.pose.orientation.x = float(message[3])
            marker.pose.orientation.y = float(message[4])
            marker.pose.orientation.z = float(message[5])
            marker.pose.orientation.w = float(message[6])
            marker.scale.x = 0.1
            marker.scale.y = 0.1
            marker.scale.z = 0.1
            marker.color.r = 0.1
            marker.color.g = 0.0
            marker.color.b = 0.0
            marker.color.a = 1.0
            marker_array.markers.append(marker)
            num += 1

        self.marker.publish(marker_array)
    
    # Transform the current waypoint into world coordinates
    def get_transform (self, current_point, odom_msg):
        # quaternion is fetched from the pose message sent 
        quat = [odom_msg.pose.pose.orientation.x, odom_msg.pose.pose.orientation.y,
                                odom_msg.pose.pose.orientation.z, odom_msg.pose.pose.orientation.w]
        # convert quaternion to roll, pitch and yaw angles 
        roll, pitch, yaw = self.q_rpy(quat)

        theta = math.atan2(current_point[1] - odom_msg.pose.pose.position.y,
                            current_point[0] - odom_msg.pose.pose.position.x)
        
        difference = theta - yaw

        distance = find_distance(current_point, [odom_msg.pose.pose.position.x, odom_msg.pose.pose.position.y])

        # Find the transformed distance 
        transformed_x = distance * math.cos(difference)
        transformed_y = distance * math.sin(difference)

        return [transformed_x, transformed_y]

    # Convert quaternion to roll, pitch and yaw angles
    def q_rpy(self, quaternion):
        x = quaternion[0]
        y = quaternion[1]
        z = quaternion[2]
        w = quaternion[3]

        roll = math.atan2(2.0 * (w * x + y * z),
                            1.0 - 2.0 * (x**2 + y**2))
        pitch = math.asin(2.0 * (w * y - z * x))
        yaw = math.atan2(2.0 * (w * z + x * y),
                            1.0 - 2.0 * (y**2 + z**2))
        return roll, pitch, yaw

        
    def pose_callback(self, pose_msg):
        # First read the data from the csv file 
        actual_position_x, actual_position_y = pose_msg.pose.pose.position.x, pose_msg.pose.pose.position.y
        lookahead_distance = 1
        min_distance = float('inf')
        min_diff = float('inf')

        tf_x = 0
        tf_y = 0
        wp_x = 0
        wp_y = 0

        csv_data = self.csv_data
        self.get_logger().info('Length of csv data is %d' % len(self.csv_data))

        for i in range (len(csv_data)):
            row = csv_data[0]

            x, y = float(row[0]), float(row[1])

            current_distance = find_distance([actual_position_x, actual_position_y], [x, y])            
            
            if current_distance < lookahead_distance and current_distance:
                diff = abs(current_distance - lookahead_distance)
                if diff < min_diff:
                    min_diff = diff
                    min_distance = current_distance
                    wp_x, wp_y = x, y
                    csv_data.remove(row)

        
        tf_x, tf_y = self.get_transform([x, y], pose_msg)

        if min_distance == 0:
            steering_angle = 1.57
        else:
            steering_angle = 2 * (tf_y) / (min_distance * min_distance)
                 
                
        drive_msg = AckermannDriveStamped()
        drive_msg.drive.speed = float(self.get_parameter('speed').value)

        drive_msg.drive.steering_angle = steering_angle


        self.get_logger().info('Setting steering angle to %f, min_distance is %f ' % (steering_angle, min_distance))

        self.drive_.publish(drive_msg)
        

def main(args=None):
    rclpy.init(args=args)
    print("PurePursuit Initialized")
    pure_pursuit_node = PurePursuit()
    rclpy.spin(pure_pursuit_node)
    pure_pursuit_node.destroy_node()
    file.close()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
