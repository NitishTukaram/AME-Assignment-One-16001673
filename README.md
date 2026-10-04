AME RoboRacer ROS 2 Foundation Assignment

**Full Name:** Nitish Tukaram
**Student ID:** 16001673

ROS 2 Distribution and Operating System

- ROS 2 Distribution: Jazzy
- Operating System: Ubuntu 24.04

How to Run the Assignment

```bash
cd ~/ros2_ws
source install/setup.bash
ros2 launch roboracer_safety_controller safety_demo.launch.py
```

Explanation of Nodes, Topics and Message Types

1. Distance Sensor Node

Node name: distance_sensor
Publishes on: /front_distance
Message type: sensor_msgs/msg/Range
Publishes a predefined sequence of distance values that simulates an obstacle approaching the vehicle and then moving away.

2. Safety Controller Node

Node name: safety_controller
Subscribes to: /front_distance
Publishes on: /cmd_vel
Message type: geometry_msgs/msg/Twist
Implements the required safety logic:
Distance ≥ 1.0 m → 1.0 m/s
0.5 m ≤ Distance < 1.0 m → 0.3 m/s
Distance < 0.5 m → 0.0 m/s


3. Vehicle Monitor Node

Node name: vehicle_monitor
Subscribes to: /cmd_vel
Prints clear vehicle state messages:
DRIVE
SLOW
STOP


Demonstration Screenshot

/home/nitish/ros2_ws/src/roboracer_safety_controller/Screenshot 1.png

/home/nitish/ros2_ws/src/roboracer_safety_controller/screenshot 2.png



References

Official ROS 2 Jazzy Tutorials: https://docs.ros.org/en/jazzy/Tutorials.html
Creating a ROS 2 workspace
Creating a Python package
Publisher and subscriber nodes
Launch files
Git and GitHub basics





