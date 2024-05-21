from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'start_client',
            default_value='false',
            description='Flag to start the kill_robot client'
        ),
        Node(
            package='control_turtlebot3',
            executable='control',
            name='control'
        ),
        Node(
            package='control_turtlebot3',
            executable='kill_robot',
            name='kill_robot',
            condition=IfCondition(LaunchConfiguration('start_client'))
        ),
    ])
