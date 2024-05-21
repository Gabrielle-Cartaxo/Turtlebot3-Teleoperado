from setuptools import find_packages, setup

package_name = 'control_turtlebot3'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/teleop_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bielle',
    maintainer_email='gabrielle.cartaxo@sou.inteli.edu.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control = control_turtlebot3.control:main',
            'kill_robot = control_turtlebot3.kill_robot:main',
            ],
    },
)
