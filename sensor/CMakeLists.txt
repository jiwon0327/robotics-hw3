cmake_minimum_required(VERSION 3.0.2)
project(sensor)
find_package(catkin REQUIRED COMPONENTS
  common_msgs
  geometry_msgs
  rospy
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES sensor
  CATKIN_DEPENDS common_msgs geometry_msgs rospy std_msgs
#  DEPENDS system_lib
)
