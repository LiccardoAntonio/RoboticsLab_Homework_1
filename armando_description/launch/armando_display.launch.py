from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.conditions import IfCondition, UnlessCondition


def generate_launch_description():
    jsp_gui = DeclareLaunchArgument(
        name='jsp_gui',
        description='Flag to enable joint_state_publisher_gui',
        default_value='true',
        choices=['true', 'false']
    )

    rviz_config_arg = DeclareLaunchArgument(
        name='rviz2_config',
        default_value=PathJoinSubstitution(
            [FindPackageShare('armando_description'), 'config', 'rviz', 'config.rviz']
        ),
        description='Absolute path to rviz config file'
    )

    package_arg = DeclareLaunchArgument(
        'urdf_package',
        description='The package where the robot description is located',
        default_value='armando_description'
    )

    model_arg = DeclareLaunchArgument(
        'urdf_package_path',
        description='The path to the robot description relative to the package root',
        default_value='urdf/arm.urdf.xacro'
    )

    description_launch_py = IncludeLaunchDescription(
        PathJoinSubstitution(
            [FindPackageShare('urdf_launch'), 'launch', 'description.launch.py']
        ),
        launch_arguments={
            'urdf_package': LaunchConfiguration('urdf_package'),
            'urdf_package_path': LaunchConfiguration('urdf_package_path')
        }.items()
    )

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('jsp_gui'))
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('jsp_gui'))
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rviz2_config')]
    )

    return LaunchDescription([
        package_arg,
        model_arg,
        jsp_gui,
        rviz_config_arg,
        description_launch_py,
        joint_state_publisher,
        joint_state_publisher_gui,
        rviz2,
    ])
