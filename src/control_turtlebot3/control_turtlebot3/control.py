import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard
from std_srvs.srv import Empty

class TeleopTurtleBot(Node):
    def __init__(self):
        super().__init__('teleop_turtlebot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.twist = Twist()
        self.speed = 2.0
        self.turn = 1.0
        self.emergency_stop = False

        self.srv = self.create_client(Empty, 'stop_robot')

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        if key == keyboard.Key.space:  # Verifica se a tecla pressionada é a barra de espaço
            self.stop_robot()

        if key == keyboard.KeyCode.from_char('q'):  # Verifica se a tecla pressionada é 'q'
            self.stop_robot()

        if self.emergency_stop:
            return

        try:
            if key.char == 'w':
                self.twist.linear.x = self.speed
                self.twist.angular.z = 0.0
            elif key.char == 's':
                self.twist.linear.x = -self.speed
                self.twist.angular.z = 0.0
            elif key.char == 'a':
                self.twist.linear.x = 0.0
                self.twist.angular.z = self.turn
            elif key.char == 'd':
                self.twist.linear.x = 0.0
                self.twist.angular.z = -self.turn

            self.publisher_.publish(self.twist)
            self.get_logger().info(f'Velocidade Linear: {self.twist.linear.x}, Velocidade Angular: {self.twist.angular.z}')
        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False

    def stop_robot(self):
        if not self.emergency_stop:
            self.emergency_stop = True
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.publisher_.publish(self.twist)
            self.get_logger().info('Parada de emergência acionada.')

            request = Empty.Request()
            self.srv.call(request)

def main(args=None):
    rclpy.init(args=args)
    teleop_turtlebot = TeleopTurtleBot()
    rclpy.spin(teleop_turtlebot)
    teleop_turtlebot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
