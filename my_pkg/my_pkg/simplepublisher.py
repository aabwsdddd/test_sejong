import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Sim_pub(Node):
    def __init__(self):
        super().__init__('simple_mpub')
        self.pub = self.create_publisher(String, 'message', 10)
        self.create_timer(1,self.publisher)

    def publisher(self):
        msg = String()
        msg.data = 'hellow'
        self.pub.publish(msg)

def test():
    print("test")

def main():
    rclpy.init()
    """node = Node('test')
    node.create_timer(1, test)"""
    node = Sim_pub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    finally:
        node.destroy_node
        rclpy.shutdown()

if __name__ == '__main__':
    main()