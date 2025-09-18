import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Turtle(Node):
	def __init__(self):
		super().__init__('turtle') #initialize the node
		self.publisher1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) #initialize the publisher
		timer_period = .5
		
		self.timer = self.create_timer(timer_period, self.timer_callback) #frequent timer for accuracy	 
		self.time = 0

	def timer_callback(self): 
		msg = Twist()
		if self.time < 12.5: 
			msg.linear.x = 2.0
			msg.angular.z = 1.0

		elif self.time >= 12.5 and self.time < 14.5:
			msg.linear.x = 0.0
			msg.angular.z = 1.57
			
		elif self.time >= 14.5 and self.time < 17.5:
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		elif self.time >= 17.5 and self.time < 30.0:
			msg.linear.x = 0.5
			msg.angular.z = 1.0
		elif self.time >= 30 and self.time < 30.5:
			msg.linear.x = 0.0
			msg.angular.z = -1.0
		elif self.time >= 30.5 and self.time < 34:
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		elif self.time >= 34 and self.time < 53.5:
			msg.linear.x = 0.8
			msg.angular.z = 1.0
		elif self.time >= 53.5 and self.time < 56.5:
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		else:
			msg.linear.x = 0.0
			msg.angular.z = 0.0
			rclpy.shutdown()
			
		self.time += 1
			
		self.publisher1.publish(msg)



			

def main(args=None):
	rclpy.init(args=args)

	turtle = Turtle()
	
	rclpy.spin(turtle)

	rclpy.shutdown()
	turtle.destroy_node()
