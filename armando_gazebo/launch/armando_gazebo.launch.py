from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    bridge_camera = Node(
        package='ros_ign_bridge',
        executable='parameter_bridge',
        arguments=[
            '/camera@sensor_msgs/msg/Image@gz.msgs.Image',
            '/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo',
            '--ros-args',
            '-r', '/camera:=/videocamera',
        ],
        output='screen'
    )

    return LaunchDescription([
        bridge_camera
    ])
