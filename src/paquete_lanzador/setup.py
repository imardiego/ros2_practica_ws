from setuptools import find_packages, setup
# añado estos import para incluir global 
import os
from glob import glob

package_name = 'paquete_lanzador'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # línea de patrón de búsqueda del fichero launch
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miguel angel rubio',
    maintainer_email='imardiego@gmail.com',
    description='Launcher integrado en un paquete',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # no añado puntos de entrada puesto que no 
            # tendremos un código de nodo 
            # solo la estructura de paquete para lanzar un nodo
        ],
    },
)


