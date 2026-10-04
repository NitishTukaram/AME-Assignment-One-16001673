from setuptools import setup
import os
from glob import glob

package_name = 'roboracer_safety_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Nitish',
    maintainer_email='nitish@example.com',
    description='RoboRacer safety controller demo',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'distance_sensor = roboracer_safety_controller.distance_sensor:main',
            'safety_controller = roboracer_safety_controller.safety_controller:main',
            'vehicle_monitor = roboracer_safety_controller.vehicle_monitor:main',
        ],
    },
)
