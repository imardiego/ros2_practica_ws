# Importamos algunos módulos launch que nos 
# interesan para poder ejecutar este lanzador
from launch import LaunchDescription
from launch_ros.actions import Node

# Comenzamos con la descripción del lanzamiento
def generate_launch_description():
    
    return LaunchDescription([
        
        # Llamamos a ambos nodos
        # Al servidor sin ningún valor
        # Al cliente con los valores de Kp,Ki,Kd
        Node(
            package='my_sim_pkg',  
            executable='simulator',  
            output='screen',    
        ),
        Node(
            package='my_genetic_pkg',
            executable='genetic',
            output='screen',
            # kp,ki,kd
            arguments=['10.0', '11.0', '12.0'],
        ),
        
    ])
    
    
    