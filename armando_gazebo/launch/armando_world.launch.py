from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    controller_type = LaunchConfiguration('controller_type')
    gui = LaunchConfiguration('gui')

    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='true',
    )

    controller_arg = DeclareLaunchArgument(
        'controller_type',
        default_value='0',
    )

    xacro_armando = os.path.join(
        get_package_share_directory('armando_description'),
        'urdf',
        'arm.urdf.xacro'
    )

    robot_description_armando_xacro = {
        'robot_description': Command(['xacro ', xacro_armando])
    }

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[
            robot_description_armando_xacro,
            {'use_sim_time': True},
        ],
    )

    empty_world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gui': gui,
            'pause': 'true',
            'gz_args': '-r empty.sdf',
        }.items(),
    )

    urdf_spawner_node = Node(
        package='ros_gz_sim',
        executable='create',
        name='urdf_spawner',
        arguments=['-topic', '/robot_description', '-entity', 'robot', '-z', '0.5', '-unpause'],
        output='screen',
    )

    position_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['position_controller', '--controller-manager', '/controller_manager'],
        condition=IfCondition(PythonExpression([controller_type, ' == 0']))
    )

    joint_trajectory_controller = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_trajectory_controller', '--controller-manager', '/controller_manager'],
        condition=IfCondition(PythonExpression([controller_type, ' == 1']))
    )

    joint_state_broadcaster = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
        output='screen'
    )

    delay_joint_state_broadcaster = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=urdf_spawner_node,
            on_exit=[joint_state_broadcaster],
        )
    )

    delay_position_controller = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=urdf_spawner_node,
            on_exit=[position_controller],
        )
    )

    delay_joint_trajectory_controller = RegisterEventHandler(
        event_handler=OnProcessExit(
            target_action=urdf_spawner_node,
            on_exit=[joint_trajectory_controller],
        )
    )

    return LaunchDescription([
        gui_arg,
        controller_arg,
        robot_state_publisher_node,
        empty_world_launch,
        urdf_spawner_node,
        delay_joint_state_broadcaster,
        delay_position_controller,
        delay_joint_trajectory_controller,
    ])
