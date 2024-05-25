from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sim_pkg',  
            executable='simulator', 
            output='screen',
            # kp, ki, kd
            arguments=['0.1888', '0.0598', '0.0011'],         
        )
    ])
   
   
    
    
    
    