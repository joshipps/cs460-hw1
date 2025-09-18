import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Turtle(Node):
	def __init__(self):
		super().__init__('turtle') #initialize the node
		self.publisher1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) #initialize the publisher
		timer_period = .2
		
		self.timer = self.create_timer(timer_period, self.timer_callback) #frequent timer for accuracy	 
		self.time = 0

	def timer_callback(self): 
		msg = Twist()
		msg.linear.x = 2.0
		msg.angular.z = 1.0	#Constant angular and linear velocity 
					#continuously moves forward and turns left
		self.time += 1		#Until
		if self.time > 32:	#When the timer increments past 32, stop movement and shutdown
			msg.linear.x = 0.0
			msg.angular.z = 0.0
			self.publisher1.publish(msg)
			rclpy.shutdown() 

		self.publisher1.publish(msg)
			


def main(args=None):
	rclpy.init(args=args)

	turtle = Turtle()
	
	rclpy.spin(turtle)

	rclpy.shutdown()
	turtle.destroy_node()
