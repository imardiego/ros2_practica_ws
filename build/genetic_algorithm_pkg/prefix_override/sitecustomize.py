import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/miguel/ros2_practica_ws/install/genetic_algorithm_pkg'
