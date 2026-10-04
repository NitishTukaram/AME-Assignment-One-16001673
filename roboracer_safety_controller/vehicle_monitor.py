#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VehicleMonitor(Node):
    def __init__(self):
        super().__init__('vehicle_monitor')
        self.subscription = self.create_subscription(
            Twist, '/cmd_vel', self.cmd_callback, 10)

    def cmd_callback(self, msg):
        speed = msg.linear.x
        if speed >= 0.9:
            state = 'DRIVE'
        elif speed > 0.0:
            state = 'SLOW'
        else:
            state = 'STOP'
        self.get_logger().info(f'Vehicle state: {state}  (speed = {speed:.1f} m/s)')

def main(args=None):
    rclpy.init(args=args)
    node = VehicleMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
