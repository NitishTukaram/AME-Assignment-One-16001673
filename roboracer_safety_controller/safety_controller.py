#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class SafetyController(Node):
    def __init__(self):
        super().__init__('safety_controller')
        self.subscription = self.create_subscription(
            Range, '/front_distance', self.distance_callback, 10)
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

    def distance_callback(self, msg):
        distance = msg.range
        cmd = Twist()
        if distance >= 1.0:
            cmd.linear.x = 1.0
        elif distance >= 0.5:
            cmd.linear.x = 0.3
        else:
            cmd.linear.x = 0.0
        self.publisher_.publish(cmd)
        self.get_logger().info(f'Distance {distance:.2f} m → velocity {cmd.linear.x:.1f} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = SafetyController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
