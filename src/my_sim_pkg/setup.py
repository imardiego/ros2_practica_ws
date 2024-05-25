from setuptools import find_packages, setup
# más tarde quizás tengamos que incluir imports aquí
package_name = 'my_sim_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # es posible que tengamos que añadir una línea 
        # búsqueda de fichero
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miguel angel rubio',
    maintainer_email='imardiego@gmail.com',
    description='Servidor de servicio de índices de rendimiento',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # tendremos que añadir aquí un punto de entrada
            'simulator = my_sim_pkg.my_sim_node:main'
            
        ],
    },
)




