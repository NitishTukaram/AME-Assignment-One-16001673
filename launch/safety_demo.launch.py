from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='roboracer_safety_controller',
            executable='distance_sensor',
            name='distance_sensor',
            output='screen'
        ),
        Node(
            package='roboracer_safety_controller',
            executable='safety_controller',
            name='safety_controller',
            output='screen'
        ),
        Node(
            package='roboracer_safety_controller',
            executable='vehicle_monitor',
            name='vehicle_monitor',
            output='screen'
        ),
    ])
