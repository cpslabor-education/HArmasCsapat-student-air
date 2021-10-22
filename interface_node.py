from rcl_interfaces import msg
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64,String,Int32

Uc_elozo = Float64()
Uc_elozo.data = 0.0

class InterfaceNode(Node):

    def __init__(self):
        super().__init__("interface_node")
        #Subsciber
        self.sub = self.create_subscription(Float64, "/beav_topic", self.cb_sub_beav_topik, 0)
        #Publisher
        self.pub_sens = self.create_publisher(Float64, "/sensor_topic", 0)
        self.get_logger().info("Inicializálás kész")
        
        


    def cb_sub_beav_topik(self, data: Float64):
        Uc = Float64()
        
        R = 1600.0
        C = 0.000001
        dt = 0.0001
        arc = dt/(dt + R*C)
        brc = (R*C)/(dt + R*C)

        Uc.data = arc*data.data + Uc.data * brc

        #Uc_elozo.data = Uc.data

        #self.get_logger().info(f"Transzformált érték: {msg.data}")
        self.pub_sens.publish(Uc)
        

def main(args=None):
    rclpy.init(args=args)
    interface_node = InterfaceNode()
    rclpy.spin(interface_node)
    interface_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
