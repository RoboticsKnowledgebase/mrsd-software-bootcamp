#!/usr/bin/env python3
"""
This file contains the class definition for tree nodes and RRT
Before you start, please read: https://arxiv.org/pdf/1105.1186.pdf
"""
import numpy as np
from numpy import linalg as LA
import math
import numpy as np
import csv
import scipy
from scipy.interpolate import splprep, splev

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PointStamped
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry, Path
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive
from nav_msgs.msg import OccupancyGrid
from tf_transformations import euler_from_quaternion

# TODO: import as you need

# class def for tree nodes
# It's up to you if you want to use this
class TreeNode(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.parent = None
        self.cost = None # only used in RRT*
        self.is_root = False
        self.steering_required = 0.0
        self.orientation_of_car = 0.0

class RRT(Node):
    def __init__(self):
        super().__init__('rrt_node')
        # topics, not saved as attributes
        # TODO: grab topics from param file, you'll need to change the yaml file
        pose_topic = "ego_racecar/odom"
        scan_topic = "/scan"
        drive_topic = '/drive'
        path_topic = '/pure_pursuit_path'
        tracked_waypoint_topic = '/waypoint_path'
        collision_detection_point_topic = '/collision_detection_point'
        sampled_point_topic = '/sampled_point'
        nearest_point_topic = '/nearest_point'
        new_point_topic = '/new_point'
        tree_topic = '/rrt_tree_viz'
        tree_points_topic = 'rrt_tree_points_viz'
        chosen_path_topic = '/rrt_chosen_path_viz'

        # you could add your own parameters to the rrt_params.yaml file,
        # and get them here as class attributes as shown above.
        self.declare_parameter('lookahead', rclpy.Parameter.Type.DOUBLE)
        self.declare_parameter('csv', rclpy.Parameter.Type.STRING)
        
        self.lookahead_distance = self.get_parameter('lookahead').value
        self.csv_filename = self.get_parameter('csv').value
        
        # read waypoints csv file
        # csv_filename = "2024-02-24_08-38-54.csv"
        x, y = self.handleCSV('/home/schittup/Projects/f1tenth/sim_ws/src/waypoint_logger/waypoints/'+self.csv_filename)
        
        # extract smooth interpolated (x,y)
        num_new_points = 10000
        self.waypoint_x, self.waypoint_y = self.interpolate_xy(x, y, num_new_points)
        self.path = Path()
        for x, y in zip(self.waypoint_x, self.waypoint_y):
            pose_msg = PoseStamped()
            pose_msg.header.frame_id='map'
            pose_msg.pose.position.x = x
            pose_msg.pose.position.y = y
            self.path.poses.append(pose_msg)

        # TODO: create subscribers
        self.scan_sub_ = self.create_subscription(
            LaserScan,
            scan_topic,
            self.scan_callback,
            1)
        self.scan_sub_
        
        self.pose_sub_ = self.create_subscription(
            #PoseStamped,
            Odometry,
            pose_topic,
            self.pose_callback,
            1)
        self.pose_sub_
        
        self.drive_sub_ = self.create_subscription(
            #PoseStamped,
            AckermannDriveStamped,
            drive_topic,
            self.drive_callback,
            1)
        self.drive_sub_

        # publishers
        # TODO: create a drive message publisher, and other publishers that you might need
        self.drive_publisher = self.create_publisher(AckermannDriveStamped, drive_topic, 10)
        self.drive_publisher
        
        self.path_pub = self.create_publisher(Path, path_topic, 10)
        self.path_pub
        
        self.tracked_waypoint_pub = self.create_publisher(PointStamped, tracked_waypoint_topic, 10)
        self.tracked_waypoint_pub
        
        self.collision_detection_point_pub = self.create_publisher(PointStamped, collision_detection_point_topic, 10)
        self.collision_detection_point_pub
        
        self.sampled_point_pub = self.create_publisher(PointStamped, sampled_point_topic, 10)
        self.sampled_point_pub
        
        self.nearest_point_pub = self.create_publisher(PointStamped, nearest_point_topic, 10)
        self.nearest_point_pub
        
        self.new_point_pub = self.create_publisher(PointStamped, new_point_topic, 10)
        self.new_point_pub
        
        self.tree_pub = self.create_publisher(Marker, tree_topic, 10)
        self.tree_pub
        
        self.tree_points_pub = self.create_publisher(Marker, tree_points_topic, 10)
        self.tree_points_pub
        
        self.chosen_path_pub = self.create_publisher(Marker, chosen_path_topic, 10)
        self.chosen_path_pub

        # class attributes
        self.angle_min = -2.3499999046325684
        self.angle_max = 2.3499999046325684
        self.angle_increment = 0.004351851995034384
        self.steering_to_curvature_scaling = 1.0
        self.prev_steering_angle = 0.0
        self.prev_timestamp = self.get_clock().now().to_msg().nanosec
        self.prev_speed = 0.0
        # TODO: maybe create your occupancy grid here
        # self.occupancy_grid = np.zeros((21, 21)) # initialize all as free space

    def handleCSV(self, csv_filename):
        x = []
        y = []
        with open(csv_filename, "r", newline="") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                x.append(float(row[0]))
                y.append(float(row[1]))
        # remove the last 1000 points so that the end point is not ahead of the start point       
        x = np.array(x[:-1000])
        y = np.array(y[:-1000])
        
        return x, y
    
    def interpolate_xy(self, x, y, num_new_points):
        # https://stackoverflow.com/questions/47948453/scipy-interpolate-splprep-error-invalid-inputs
        okay = np.where(np.abs(np.diff(x)) + np.abs(np.diff(y)) > 0)
        x = np.r_[x[okay], x[-1], x[0]]
        y = np.r_[y[okay], y[-1], y[0]]

        jump = np.sqrt(np.diff(x)**2 + np.diff(y)**2) 
        smooth_jump = scipy.ndimage.gaussian_filter1d(jump, 5, mode='wrap')  # window of size 5 is arbitrary
        limit = 2*np.median(smooth_jump)    # factor 2 is arbitrary
        x, y = x[:-1], y[:-1]
        x = x[(jump > 0) & (smooth_jump < limit)]
        y = y[(jump > 0) & (smooth_jump < limit)]
        x = np.append(x, [x[0]])
        y = np.append(y, [y[0]])
        
        # https://stackoverflow.com/questions/33962717/interpolating-a-closed-curve-using-scipy
        tck, u = splprep([x, y], s=10, per=True) # u is the parametrization of curve. so u is in range [0, 1)
        new_points = splev(np.linspace(0, 1, num_new_points), tck) # new_points[0] are the x coordinates and new_points[1] are the corresponding y
        
        return new_points[0], new_points[1]
    
    def find_waypoint_to_track(self, current_x, current_y):
        dx = self.waypoint_x - current_x
        dy = self.waypoint_y - current_y
        distance_from_current_position = np.hypot(dx, dy)
        nearest_waypoint_to_current_position_idx = np.argmin(distance_from_current_position)
        
        # self.lookahead_distance = 1.0
        idx = nearest_waypoint_to_current_position_idx+1
        while distance_from_current_position[idx] < self.lookahead_distance:
            idx += 1
            # end of the loop case
            if idx > len(self.waypoint_x)-1:
                idx = 0
        return (self.waypoint_x[idx], self.waypoint_y[idx]), distance_from_current_position[idx]
    
    def baselink_to_map(self, point_car_coord, map_x, map_y, orientaton):
        # rotation
        theta = -orientaton
        rotated_x = np.cos(theta)*point_car_coord[0] + np.sin(theta)*point_car_coord[1]
        rotated_y = -np.sin(theta)*point_car_coord[0] + np.cos(theta)*point_car_coord[1]
        # rotated_x = np.cos(theta)*(point_car_coord[0] + 0.2) + np.sin(theta)*point_car_coord[1]
        # rotated_y = -np.sin(theta)*(point_car_coord[0] + 0.2) + np.cos(theta)*point_car_coord[1]
        
        # translation
        translated_x = map_x + rotated_x
        translated_y = map_y + rotated_y
        
        return translated_x, translated_y
    
    def map_to_baselink(self, waypoint_map_coord, map_x, map_y, orientaton):
        # translation
        translated_x = waypoint_map_coord[0] - map_x
        translated_y = waypoint_map_coord[1] - map_y
        
        # rotation
        theta = orientaton
        rotated_x = np.cos(theta)*translated_x + np.sin(theta)*translated_y
        rotated_y = -np.sin(theta)*translated_x + np.cos(theta)*translated_y
        
        return rotated_x, rotated_y # rotated_x - 0.2, rotated_y
    
    def convert_lidar_scan_to_local_coordinates(self):
        all_angles = np.arange(self.angle_min, self.angle_max, self.angle_increment)
        x_component = np.cos(all_angles)
        y_component = np.sin(all_angles)
        ranges_as_points_x = x_component*self.ranges
        ranges_as_points_y = y_component*self.ranges
        # print("all_angles: ", len(all_angles))
        # print("ranges: ", len(self.ranges))
        # selecting 180 degrees fov
        min_index = int((np.radians(-90) - self.angle_min)/self.angle_increment)
        max_index = int((np.radians(90) - self.angle_min)/self.angle_increment)
        # print("min index   max index: ", min_index, max_index)
        ranges_as_points_x = ranges_as_points_x[min_index:max_index+1]
        ranges_as_points_y = ranges_as_points_y[min_index:max_index+1]
        # print('processed ranges: ', ranges_as_points_x[0], ranges_as_points_y[0])
        # print('processed ranges: ', ranges_as_points_x[-1], ranges_as_points_y[-1])
        return ranges_as_points_x, ranges_as_points_y
    
    def drive_callback(self, drive_msg):
        self.prev_timestamp = drive_msg.header.stamp.nanosec
        self.prev_steering_angle = drive_msg.drive.steering_angle
        self.prev_speed = drive_msg.drive.speed
        print("aa raha hu idhar: ", self.prev_timestamp, self.prev_steering_angle)
    
    def scan_callback(self, scan_msg):
        """
        LaserScan callback, you should update your occupancy grid here

        Args: 
            scan_msg (LaserScan): incoming message from subscribed topic
        Returns:

        """
        self.ranges = scan_msg.ranges
        

    def pose_callback(self, pose_msg):
        """
        The pose callback when subscribed to particle filter's inferred pose
        Here is where the main RRT loop happens

        Args: 
            pose_msg (PoseStamped): incoming message from subscribed topic
        Returns:

        """
        
        rrt_tree_msg = Marker()
        rrt_tree_msg.header = pose_msg.header
        rrt_tree_msg.id = 0
        rrt_tree_msg.type = Marker.LINE_LIST
        rrt_tree_msg.action = Marker.ADD
        rrt_tree_msg.color.b = 1.0
        rrt_tree_msg.color.a = 1.0
        rrt_tree_msg.scale.x = 0.01
        
        rrt_points_msg = Marker()
        rrt_points_msg.header = pose_msg.header
        rrt_points_msg.id = 1
        rrt_points_msg.type = Marker.POINTS
        rrt_points_msg.action = Marker.ADD
        rrt_points_msg.color.r = 0.5
        rrt_points_msg.color.g = 0.4
        rrt_points_msg.color.b = 0.8
        rrt_points_msg.color.a = 1.0
        rrt_points_msg.scale.x = 0.1
        rrt_points_msg.scale.y = 0.1
        
        chosen_path_points_msg = Marker()
        chosen_path_points_msg.header = pose_msg.header
        chosen_path_points_msg.id = 2
        chosen_path_points_msg.type = Marker.POINTS
        chosen_path_points_msg.action = Marker.ADD
        chosen_path_points_msg.color.g = 1.0
        chosen_path_points_msg.color.a = 1.0
        chosen_path_points_msg.scale.x = 0.3
        chosen_path_points_msg.scale.y = 0.3
                    
        self.ranges_as_points_x, self.ranges_as_points_y = self.convert_lidar_scan_to_local_coordinates()
        
        x_orig = pose_msg.pose.pose.position.x
        y_orig = pose_msg.pose.pose.position.y
        quaternion = np.array([pose_msg.pose.pose.orientation.x, 
                            pose_msg.pose.pose.orientation.y, 
                            pose_msg.pose.pose.orientation.z, 
                            pose_msg.pose.pose.orientation.w])

        euler = euler_from_quaternion(quaternion)
        orientation_orig = euler[2]
        
        parent_node = TreeNode()
        # local coord
        parent_node.x = 0.0
        parent_node.y = 0.0
        parent_node.parent = None
        parent_node.is_root = True
        
        all_nodes = [parent_node]
        
        self.nearest_node_to_goal_node = parent_node
        self.nearest_node_to_goal_node_distance = 1000
        
        waypoint_to_track, distance_of_car_from_waypoint = self.find_waypoint_to_track(x_orig, y_orig)
        
        # apply rotation and translation
        waypoint_to_track_in_baselink_coord = self.map_to_baselink(waypoint_to_track, x_orig, y_orig, orientation_orig)
        # print("Waypoint to track in local coord: ", waypoint_to_track_in_baselink_coord)
        
        self.path.header = pose_msg.header
        self.path_pub.publish(self.path)
        
        waypoint_as_pose_msg = PointStamped()
        waypoint_as_pose_msg.header = pose_msg.header
        waypoint_as_pose_msg.point.x = waypoint_to_track[0]
        waypoint_as_pose_msg.point.y = waypoint_to_track[1]
        self.tracked_waypoint_pub.publish(waypoint_as_pose_msg)
        
        
        
        goal_node = TreeNode()
        # local coord
        goal_node.x = waypoint_to_track_in_baselink_coord[0]
        goal_node.y = waypoint_to_track_in_baselink_coord[1]
        goal_node.parent = []
        
        collision_flag, collision_x, collision_y = self.check_collision(parent_node, goal_node)
        collision_x, collision_y = self.baselink_to_map([collision_x, collision_y], x_orig, y_orig, orientation_orig)
        collision_detection_point_msg = PointStamped()
        collision_detection_point_msg.header = pose_msg.header
        collision_detection_point_msg.point.x = collision_x
        collision_detection_point_msg.point.y = collision_y
        self.collision_detection_point_pub.publish(collision_detection_point_msg)
        
        # print("collision hai?: ", collision_flag)
        if collision_flag:
            print("nahi mila")
            for i in range(0, 100, 1):
                x_rand = self.sample()
                sampled_x_map_coord, sampled_y_map_coord = self.baselink_to_map(x_rand, x_orig, y_orig, orientation_orig)
                sampled_point_msg = PointStamped()
                sampled_point_msg.header = pose_msg.header
                sampled_point_msg.point.x = sampled_x_map_coord
                sampled_point_msg.point.y = sampled_y_map_coord
                self.sampled_point_pub.publish(sampled_point_msg)
                x_near_idx = self.nearest(all_nodes, x_rand)
                x_near = all_nodes[x_near_idx]
                # x_near.x=0.73
                # x_near.y=0.49
                nearest_x_map_coord, nearest_y_map_coord = self.baselink_to_map([x_near.x, x_near.y], x_orig, y_orig, orientation_orig)
                nearest_point_msg = PointStamped()
                nearest_point_msg.header = pose_msg.header
                nearest_point_msg.point.x = nearest_x_map_coord
                nearest_point_msg.point.y = nearest_y_map_coord
                self.nearest_point_pub.publish(nearest_point_msg)
                # exit()
                x_new = self.steer(x_near, x_rand)
                # x_new.x=1.2
                # x_new.y=0.68
                new_x_map_coord, new_y_map_coord = self.baselink_to_map([x_new.x, x_new.y], x_orig, y_orig, orientation_orig)
                new_point_msg = PointStamped()
                new_point_msg.header = pose_msg.header
                new_point_msg.point.x = new_x_map_coord
                new_point_msg.point.y = new_y_map_coord
                self.new_point_pub.publish(new_point_msg)
                # exit()
                import time
                if not self.check_collision(x_near, x_new)[0]:
                    # print(x_near.x, x_near.y, x_new.x, x_new.y)
                    new_node = TreeNode()
                    new_node.x = x_new.x
                    new_node.y = x_new.y
                    new_node.parent = x_near
                    new_node.orientation_of_car = np.arctan((x_new.y-x_near.y)/(x_new.x-x_near.x))
                    new_node.steering_required = abs(new_node.orientation_of_car - x_near.orientation_of_car)
                    print("new orientation: ", new_node.orientation_of_car)
                    print("steering required: ", new_node.steering_required)
                    
                    p = Point()
                    p.x = new_x_map_coord
                    p.y = new_y_map_coord
                    p.z = 0.0
                    rrt_points_msg.points.append(p)
                    rrt_tree_msg.points.append(p)
                    p = Point()
                    p.x = nearest_x_map_coord
                    p.y = nearest_y_map_coord
                    p.z = 0.0
                    rrt_tree_msg.points.append(p)
                    self.tree_pub.publish(rrt_tree_msg)
                    self.tree_points_pub.publish(rrt_points_msg)
                    
                    all_nodes.append(new_node)
                    
                    dist_to_goal = np.hypot(new_node.x-goal_node.x, new_node.y-goal_node.y)
                    if dist_to_goal < self.nearest_node_to_goal_node_distance:
                        self.nearest_node_to_goal_node_distance = dist_to_goal
                        self.nearest_node_to_goal_node = new_node
                    # time.sleep(5)
                    
                    if self.is_goal(new_node, goal_node):
                        goal_node.parent.append(new_node)
                        # print('mil gaya goal')
                        # time.sleep(5)
                        # break
                    # if not self.check_collision(new_node, goal_node)[0]:
                    #     # print(new_node.x, new_node.y, )
                    #     goal_node.parent = new_node
                    #     print('mil gaya collision free goal')
                    #     # exit()
                    #     break
        
            # print(len(goal_node.parent))
            # time.sleep(5)
            min_effort = 1000000
            min_effort_path = None
            if len(goal_node.parent) != 0:
                print("Non min effort path: ", i)
                for node in goal_node.parent:
                    path, effort = self.find_path(node)
                    if effort < min_effort:
                        min_effort = effort
                        min_effort_path = path
                    print(path)
                # time.sleep(5)
            else:
                print("min effore path: ", i)
                path, effort = self.find_path(self.nearest_node_to_goal_node)
                if effort < min_effort:
                    min_effort = effort
                    min_effort_path = path
            if len(min_effort_path) == 0:
                min_effort_path = [[1e-6, 1e-6]]
            
            for path_points in min_effort_path:
                path_x_map_coord, path_y_map_coord = self.baselink_to_map([path_points[0], path_points[1]], x_orig, y_orig, orientation_orig)
                p = Point()
                p.x = path_x_map_coord
                p.y = path_y_map_coord
                p.z = 0.0
                chosen_path_points_msg.points.append(p)
            self.chosen_path_pub.publish(chosen_path_points_msg)
            
            # TODO: calculate curvature/steering angle
            alpha = np.arctan(min_effort_path[-1][1]/min_effort_path[-1][0])
            print("alpha: ", alpha)
            distance_of_car_from_selected_point = np.hypot(min_effort_path[-1][1], min_effort_path[-1][0])
            curvature = (2*distance_of_car_from_selected_point*np.sin(alpha))/(distance_of_car_from_selected_point**2)
            print("curvature: ", curvature)
            desired_steering_angle = self.steering_to_curvature_scaling * curvature

            # TODO: publish drive message, don't forget to limit the steering angle.
            if desired_steering_angle > 0.35:
                desired_steering_angle = 0.35
            elif desired_steering_angle < -0.35:
                desired_steering_angle = -0.35
                
            drive_msg = AckermannDriveStamped()
            drive_msg.header.stamp = self.get_clock().now().to_msg()
            steering_angle = desired_steering_angle
            drive_msg.drive.steering_angle = steering_angle
            drive_msg.drive.speed = 0.0
            self.drive_publisher.publish(drive_msg)
            time.sleep(10)
        else:
            # TODO: calculate curvature/steering angle
            alpha = np.arctan(waypoint_to_track_in_baselink_coord[1]/waypoint_to_track_in_baselink_coord[0])
            print("alpha: ", alpha)
            curvature = (2*distance_of_car_from_waypoint*np.sin(alpha))/(distance_of_car_from_waypoint**2)
            print("curvature: ", curvature)
            desired_steering_angle = self.steering_to_curvature_scaling * curvature

            # TODO: publish drive message, don't forget to limit the steering angle.
            if desired_steering_angle > 0.35:
                desired_steering_angle = 0.35
            elif desired_steering_angle < -0.35:
                desired_steering_angle = -0.35
                
            drive_msg = AckermannDriveStamped()
            drive_msg.header.stamp = self.get_clock().now().to_msg()
            # print("desired: ", desired_steering_angle)
            # print("time diff: ", drive_msg.header.stamp.nanosec-self.prev_timestamp)
            # print('angle correction: ', desired_steering_angle-self.prev_steering_angle) 
            # print("correction: ", ((desired_steering_angle-self.prev_steering_angle)*0.01))
            # print("previous: ", self.prev_steering_angle)
            steering_angle = desired_steering_angle
            drive_msg.drive.steering_angle = steering_angle
            drive_msg.drive.speed = 0.0
            self.drive_publisher.publish(drive_msg)
            # exit()
        return None

    def sample(self):
        """
        This method should randomly sample the free space, and returns a viable point

        Args:
        Returns:
            (x, y) (float float): a tuple representing the sampled point

        """
        # x = np.random.uniform(0.5, self.lookahead_distance+0.3) # 0.5 is to offset from the rear axle to front axle
        new_range = 10
        old_low_limit = 0.9
        old_upper_limit = self.lookahead_distance+0.3
        old_range = old_upper_limit-old_low_limit
        rand_num = np.random.randint(0, 10)
        x = (abs(old_range/new_range)*rand_num) + old_low_limit
        
        # y = np.random.uniform(-1, 1)
        y = np.random.randint(-10, 10)/10
        print(x, y)
        return (x, y)

    def nearest(self, tree, sampled_point):
        """
        This method should return the nearest node on the tree to the sampled point

        Args:
            tree ([]): the current RRT tree
            sampled_point (tuple of (float, float)): point sampled in free space
        Returns:
            nearest_node (int): index of neareset node on the tree
        """
        nearest_node = -1
        nearest_distance = 10000
        for idx, node in enumerate(tree):
            dist = np.hypot(node.x-sampled_point[0], node.y-sampled_point[1])
            # print([node.x, node.y], sampled_point, dist)
            if dist < nearest_distance:
                nearest_distance = dist
                nearest_node = idx
        return nearest_node

    def steer(self, nearest_node, sampled_point):
        """
        This method should return a point in the viable set such that it is closer 
        to the nearest_node than sampled_point is.

        Args:
            nearest_node (Node): nearest node on the tree to the sampled point
            sampled_point (tuple of (float, float)): sampled point
        Returns:
            new_node (Node): new node created from steering
        """
        new_node = TreeNode()
        #https://math.stackexchange.com/questions/2045174/how-to-find-a-point-between-two-points-with-given-distance
        dist_between_near_and_sampled = np.hypot(nearest_node.x-sampled_point[0], nearest_node.y-sampled_point[1])
        # print("dist_between_near_and_sampled: ", dist_between_near_and_sampled)
        random_dist = np.random.uniform(0.9, max(0.9, dist_between_near_and_sampled/2))
        new_node.x = nearest_node.x + ((random_dist/dist_between_near_and_sampled)*(sampled_point[0]-nearest_node.x))
        new_node.y = nearest_node.y + ((random_dist/dist_between_near_and_sampled)*(sampled_point[1]-nearest_node.y))
        new_node.parent = nearest_node
        return new_node

    def check_collision(self, nearest_node, new_node):
        """
        This method should return whether the path between nearest and new_node is
        collision free.

        Args:
            nearest (Node): nearest node on the tree
            new_node (Node): new node from steering
        Returns:
            collision (bool): whether the path between the two nodes are in collision
                              with the occupancy grid
        """
        xa, ya = nearest_node.x, nearest_node.y
        xb, yb = new_node.x, new_node.y
        for xc, yc in zip(self.ranges_as_points_x, self.ranges_as_points_y):
            # (xb-xa)(yc-ya)-(yb-ya)(xc-xa)/sqrt((xb-xa)**2(yb-ya)**2)
            dist_from_line = self.dist(xa, ya, xb, yb, xc, yc)#np.abs(((xb-xa)*(yc-ya))-((yb-ya)*(xc-xa))/np.sqrt(((xb-xa)**2)*((yb-ya)**2)))
            if dist_from_line < 0.2:
                # print(dist_from_line)
                # print("dist from line: ", xa, ya, xb, yb, xc, yc)
                return True, xc, yc
        return False, 0.0, 0.0

    def dist(self, x1, y1, x2, y2, x3, y3): # x3,y3 is the point
        # https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
        px = x2-x1
        py = y2-y1

        norm = px*px + py*py

        u =  ((x3 - x1) * px + (y3 - y1) * py) / float(norm)

        if u > 1:
            u = 1
        elif u < 0:
            u = 0

        x = x1 + u * px
        y = y1 + u * py

        dx = x - x3
        dy = y - y3

        # Note: If the actual distance does not matter,
        # if you only want to compare what this function
        # returns to other results of this function, you
        # can just return the squared distance instead
        # (i.e. remove the sqrt) to gain a little performance

        dist = (dx*dx + dy*dy)**.5

        return dist

    def is_goal(self, latest_added_node, goal_node):
        """
        This method should return whether the latest added node is close enough
        to the goal.

        Args:
            latest_added_node (Node): latest added node on the tree
            goal_x (double): x coordinate of the current goal
            goal_y (double): y coordinate of the current goal
        Returns:
            close_enough (bool): true if node is close enoughg to the goal
        """
        if np.hypot(latest_added_node.x-goal_node.x, latest_added_node.y-goal_node.y) < 0.3:
            return True
        return False

    def find_path(self, node): # def find_path(self, tree, latest_added_node):
        """
        This method returns a path as a list of Nodes connecting the starting point to
        the goal once the latest added node is close enough to the goal

        Args:
            tree ([]): current tree as a list of Nodes
            latest_added_node (Node): latest added node in the tree
        Returns:
            path ([]): valid path as a list of Nodes
        """
        path = []
        effort = 0
        while not node.is_root:
            path.append((node.x, node.y))
            effort+=node.steering_required
            node = node.parent
        return path, effort



    # The following methods are needed for RRT* and not RRT
    def cost(self, tree, node):
        """
        This method should return the cost of a node

        Args:
            node (Node): the current node the cost is calculated for
        Returns:
            cost (float): the cost value of the node
        """
        return 0

    def line_cost(self, n1, n2):
        """
        This method should return the cost of the straight line between n1 and n2

        Args:
            n1 (Node): node at one end of the straight line
            n2 (Node): node at the other end of the straint line
        Returns:
            cost (float): the cost value of the line
        """
        return 0

    def near(self, tree, node):
        """
        This method should return the neighborhood of nodes around the given node

        Args:
            tree ([]): current tree as a list of Nodes
            node (Node): current node we're finding neighbors for
        Returns:
            neighborhood ([]): neighborhood of nodes as a list of Nodes
        """
        neighborhood = []
        return neighborhood

def main(args=None):
    rclpy.init(args=args)
    print("RRT Initialized")
    rrt_node = RRT()
    rclpy.spin(rrt_node)

    rrt_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
