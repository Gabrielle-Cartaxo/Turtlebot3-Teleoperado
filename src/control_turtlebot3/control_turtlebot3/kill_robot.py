import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class StopRobotClient(Node):
    def __init__(self):
        super().__init__('stop_robot_client')
        self.client = self.create_client(Empty, 'stop_robot')
        # Remova a chamada para self.stop_robot() no __init__

    def stop_robot(self):
        self.future = self.client.call_async(Empty.Request())
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            self.get_logger().info('Robô parado com sucesso.')
        else:
            self.get_logger().error('Falha ao parar o robô.')

def main(args=None):
    rclpy.init(args=args)
    stop_robot_client = StopRobotClient()
    rclpy.spin(stop_robot_client) 
    rclpy.shutdown()

if __name__ == '__main__':
    main()
