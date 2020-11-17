cmake_minimum_required(VERSION 3.0.2)
project(algorithm)

find_package(catkin REQUIRED COMPONENTS
  common_msgs
  geometry_msgs
  rospy
  std_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES algorithm
CATKIN_DEPENDS common_msgs geometry_msgs rospy std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
