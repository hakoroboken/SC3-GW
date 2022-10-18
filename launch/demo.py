from launch import LaunchDescription , actions
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os.path


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sc3_gw',
            executable='sc3_gw_server',
            parameters=[{'nic' : 'wlp3s0'} , 
                        {'c1' : 'Smart'} , 
                        {'c2' : 'Controller 3'} , 
                        {'s1' : 'power'} , 
                        {'s2' : "slider"} , 
                        {'debug' : False}],
        ),
    ])
