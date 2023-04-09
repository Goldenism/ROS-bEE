cmake_minimum_required(VERSION 3.0.2)
project(bee_foraging)


## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation  # Required for custom messages and services
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  BeeForagingAction.msg
  BeeForagingResult.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  BeeForaging.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
)

## Define catkin exports
catkin_package(
  CATKIN_DEPENDS
  rospy
  std_msgs
  message_runtime  # Required for custom messages and services
)


## Include the headers
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

