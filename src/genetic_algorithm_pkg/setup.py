from setuptools import find_packages, setup
# más adelante seguramente tendré que hacer algún import aquí
# introduzco modulo que encuentra los nombres de ruta
# que coinciden con un patrón específico de acuerdo con las 
# reglas utilizadas por el shell de Unix
#from glob import glob

package_name = 'genetic_algorithm_pkg'

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
        #('share/{}'.format(package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miguel',
    maintainer_email='imardiego@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'genetic = genetic_algorithm_pkg.genetic_algorithm_node:main'
        ],
    },
)
