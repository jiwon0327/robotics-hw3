cmake_minimum_required(VERSION 3.0.2)
project(common_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  std_msgs
)

add_message_files(
	FILES
	cm.msg
)

generate_messages(
DEPENDENCIES
geometry_msgs
std_msgs
)
catkin_package(
CATKIN_DEPENDS geometry_msgs rospy std_msgs
)
