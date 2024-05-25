from setuptools import find_packages, setup
# más adelante seguramente tendré que hacer algún import aquí
# introduzco modulo que encuentra los nombres de ruta
# que coinciden con un patrón específico de acuerdo con las 
# reglas utilizadas por el shell de Unix
from glob import glob

package_name = 'my_genetic_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # deberé meter aquí una línea de búsqueda
        # le digo como buscar el fichero de lanzamiento
        ('share/{}'.format(package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],    
    zip_safe=True,
    maintainer='miguel angel rubio',
    maintainer_email='imardiego@gmail.com',
    description='Cliente de servicio de índices de rendimiento',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # cuando tenga hecho el node.py 
            # debo introducir aquí un punto de entrada
            # significa que a través de genetic, llamo a la 
            # función main del fichero que codifica al nodo
            # my_genetic_node.py que se encuentra en el paquete
            # my_genetic_pkg
            'genetic = my_genetic_pkg.my_genetic_node:main'
        ],
    },
)







