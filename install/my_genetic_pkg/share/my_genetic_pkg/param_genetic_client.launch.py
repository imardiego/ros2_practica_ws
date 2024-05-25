from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
    	    package='my_genetic_pkg',
            executable='genetic',
            output='screen',
            # kp, ki, kd
            arguments=['10.0', '11.0', '12.0'],
            parameters=[
                {'my_parameter':'earth'}
            ],
	    )
    ])
