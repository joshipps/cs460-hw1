import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Turtle(Node):
	def __init__(self):
		super().__init__('turtle') #initialize the node
		self.publisher1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) #initialize the publisher
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback) #frequent timer for accuracy	 
		self.time = 0
		
	def create_twist(self, X, Z):
		msg = Twist()
		msg.linear.x = X
		msg.angular.z = Z
		return msg
		
	def get_twist_msg(self):
		if self.time < 5:	#First 5 seconds, draw a line
			msg = self.create_twist(1.0, 0.0)
		elif self.time >= 5 and self.time < 7: #turn left 90 degrees
			msg = self.create_twist(0.0, 1.58)
		elif self.time >= 7 and self.time < 17:	#draw line for 10 seconds
			msg = self.create_twist(1.0, 0.0)
		elif self.time >= 17 and self.time < 19: #turn left
			msg = self.create_twist(0.0, 1.58)
		elif self.time >= 19 and self.time < 24): #draw line for 5 seconds
			msg = self.create_twist(1.0, 0.0)
		elif self.time >= 24 and self.time < 26: #turn left
			msg = self.create_twist(0.0, 1.58)
		elif self.time >= 26 and self.time < 36: #draw line for 10sec to finish rectangle
			msg = self.create_twist(1.0, 0.0)
		else:	#after 37 seconds, stop and shutdown
			msg = self.create_twist(0.0, 0.0)
			rclpy.shutdown()
		return msg

	def timer_callback(self): 
		msg = self.get_twist_msg()
		self.time += 1
		self.publisher1.publish(msg)



def main(args=None):
	rclpy.init(args=args)

	turtle  = Turtle()
	rclpy.spin(turtle)

	turtle.destroy_node()
	rclpy.shutdown()

