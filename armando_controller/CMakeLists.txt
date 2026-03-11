cmake_minimum_required(VERSION 3.8)
project(armando_controller)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(trajectory_msgs REQUIRED)

add_executable(arm_controller_node src/arm_controller_node.cpp)

ament_target_dependencies(
  arm_controller_node
  rclcpp
  sensor_msgs
  std_msgs
  trajectory_msgs
)

install(TARGETS
  arm_controller_node
  DESTINATION lib/${PROJECT_NAME}
)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
