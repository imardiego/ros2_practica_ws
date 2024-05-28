from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
    	    package='genetic_algorithm_pkg',
            executable='genetic',
            output='screen',
            # kp, ki, kd
            #arguments=['10.0', '11.0', '12.0'],
            parameters=[
                {'population_size':100},
                {'generations':500},
                {'mutation_rate':0.18},
                {'crossover_rate':0.33},
            ],
	    )
    ])
