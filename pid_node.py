from rcl_interfaces import msg
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64,String,Int32
import random

sens = Float64()
rend_elozo = Float64()
rend_elozo.data = 0.0
integral = Float64()
integral.data = 0.0
der = Float64()
der.data = 0.0
rend = Float64()
rend.data = 0.0
i = Float64()
i.data = 0.0

class PidNode(Node):

    def __init__(self):
        super().__init__("pid_node")
        #Subscriber
        self.sub = self.create_subscription(Float64, "/sensor_topic", self.cb_sub_sens_topic, 0)
        #Publisher
        self.pub_beav_topic = self.create_publisher(Float64, "/beav_topic", 0)
        self.pub_masik_topic = self.create_publisher(Float64, "/masik_sens_topic", 0)
        #Timer
        self.pub_timer = self.create_timer(0.0001, self.cb_timer)
        #Értesítés a felhaználónak
        self.get_logger().info("Kész az inicializálás!")
        
    def cb_sub_sens_topic(self,data:Float64):
        sens.data = data.data
        
    def cb_timer(self):
        KP = 0.5
        KI = 1.0
        KD = 0.0
        
        szab = Float64()

        if i.data < 5.0:
            ref = 5.0
            i.data += 0.001
        elif 5.0 < i.data < 10.0:
            ref = 10.0
            i.data += 0.001
        elif 10.0 < i.data < 15.0:
            ref = 15.0
            i.data += 0.001
        elif 15.0 < i.data < 20.0:
            ref = 10.0
            i.data += 0.001
        elif 20.0 < i.data:
            ref = 5.0
            i.data = 0.0
                
        rend.data = ref - sens.data

        integral.data += (rend.data + rend_elozo.data) * 0.5
        der.data = rend.data - rend_elozo.data
        szab.data = KP*rend.data + KI*integral.data + KD*der.data
        rend_elozo.data = rend.data
        
        self.pub_beav_topic.publish(szab)
        self.pub_masik_topic.publish(sens)

        #Random számok
        #msg_random = Float64()
        #msg_random.data = random.random()
        #self.pub_interface_topic.publish(msg_random)     

def main(args=None):
    rclpy.init(args=args)
    pid_node = PidNode()
    rclpy.spin(pid_node)
    pid_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
