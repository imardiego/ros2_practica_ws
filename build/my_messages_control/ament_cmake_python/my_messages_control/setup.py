from setuptools import find_packages
from setuptools import setup

setup(
    name='my_messages_control',
    version='0.0.0',
    packages=find_packages(
        include=('my_messages_control', 'my_messages_control.*')),
)
