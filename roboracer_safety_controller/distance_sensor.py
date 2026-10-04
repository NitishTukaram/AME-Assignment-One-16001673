#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range

class DistanceSensor(Node):
    def __init__(self):
        super().__init__('distance_sensor')
        self.publisher_ = self.create_publisher(Range, '/front_distance', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        # Sequence: obstacle approaches then moves away
        self.distances = [2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.6, 0.4, 0.3, 0.2,
                          0.3, 0.5, 0.7, 0.9, 1.1, 1.4, 1.7, 2.0]
        self.index = 0

    def timer_callback(self):
        msg = Range()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'front_sonar'
        msg.radiation_type = Range.ULTRASOUND
        msg.field_of_view = 0.5
        msg.min_range = 0.1
        msg.max_range = 10.0
        msg.range = float(self.distances[self.index])
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published distance: {msg.range:.2f} m')
        self.index = (self.index + 1) % len(self.distances)

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSensor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
