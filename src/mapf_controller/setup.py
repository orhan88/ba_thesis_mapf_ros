from setuptools import setup

package_name = 'mapf_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='orchan',
    maintainer_email='orchan.heupel@gmx.de',
    description='MAPF Controller',
    license='Free to use',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "controller = mapf_controller.__main__:run"
        ],
    },
)
