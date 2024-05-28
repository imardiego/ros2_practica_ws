# Importamos algunos módulos launch que nos 
# interesan para poder ejecutar este lanzador
from launch import LaunchDescription
from launch_ros.actions import Node

# Comenzamos con la descripción del lanzamiento
def generate_launch_description():
    
    return LaunchDescription([
        
        
        Node(
            package='sim_pkg',  
            executable='simulator',  
            output='screen',    
        ),
        Node(
            package='genetic_algorithm_pkg',
            executable='genetic',
            output='screen',
            # si no pongo ni argumentos ni parámetros
            # toma los que tenga por defecto en el código inicial
        ),
        
    ])
    
    
    