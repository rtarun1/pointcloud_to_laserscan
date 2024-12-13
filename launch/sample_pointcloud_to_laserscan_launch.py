from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        
        Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            # remappings=[('cloud_in', '/livox/lidar'),
            #             ('scan', '/livox/scan')],
            parameters=[{
                'target_frame': 'laser_frame',
                'transform_tolerance': 0.01,
                'min_height': 0.1, #0
                'max_height': 2.0, #1
                'angle_min': -3.14, # -M_PI/ 2-1.5708
                'angle_max': 3.14, # M_PI/2
                'angle_increment': 0.0087, # M_PI/360.0
                'scan_time': 0.3333,
                'range_min': 1.45,
                'range_max': 50.0,
                'use_inf': True,
                'inf_epsilon': 1.0
            }],
            name='pointcloud_to_laserscan'
        )
    ])