# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/diogo/wheeled_robot_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/diogo/wheeled_robot_ws/build

# Utility rule file for run_tests_aruco_detect_rostest_test_aruco_images.test.

# Include the progress variables for this target.
include aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/progress.make

aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test:
	cd /home/diogo/wheeled_robot_ws/build/aruco_detect && ../catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/catkin/cmake/test/run_tests.py /home/diogo/wheeled_robot_ws/build/test_results/aruco_detect/rostest-test_aruco_images.xml "/opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/diogo/wheeled_robot_ws/src/aruco_detect --package=aruco_detect --results-filename test_aruco_images.xml --results-base-dir \"/home/diogo/wheeled_robot_ws/build/test_results\" /home/diogo/wheeled_robot_ws/src/aruco_detect/test/aruco_images.test "

run_tests_aruco_detect_rostest_test_aruco_images.test: aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test
run_tests_aruco_detect_rostest_test_aruco_images.test: aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/build.make

.PHONY : run_tests_aruco_detect_rostest_test_aruco_images.test

# Rule to build all files generated by this target.
aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/build: run_tests_aruco_detect_rostest_test_aruco_images.test

.PHONY : aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/build

aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/clean:
	cd /home/diogo/wheeled_robot_ws/build/aruco_detect && $(CMAKE_COMMAND) -P CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/cmake_clean.cmake
.PHONY : aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/clean

aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/depend:
	cd /home/diogo/wheeled_robot_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/diogo/wheeled_robot_ws/src /home/diogo/wheeled_robot_ws/src/aruco_detect /home/diogo/wheeled_robot_ws/build /home/diogo/wheeled_robot_ws/build/aruco_detect /home/diogo/wheeled_robot_ws/build/aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : aruco_detect/CMakeFiles/run_tests_aruco_detect_rostest_test_aruco_images.test.dir/depend

