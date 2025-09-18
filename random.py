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
		if self.time < 13: #Outer circle
			msg.linear.x = 2.0
			msg.angular.z = 1.0

		elif self.time >= 13 and self.time < 15: #Turning inward
			msg.linear.x = 0.0
			msg.angular.z = 1.57
			
		elif self.time >= 15 and self.time < 18: #Moving in
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		elif self.time >= 18 and self.time < 31.0: #Small inner circle
			msg.linear.x = 0.5
			msg.angular.z = 1.0
		elif self.time >= 31 and self.time < 31.5:  #Turning out slightly
			msg.linear.x = 0.0
			msg.angular.z = -1.0
		elif self.time >= 31.5 and self.time < 34.5:  #First connection of inner circles
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		elif self.time >= 34.5 and self.time < 54.5:  #Large inner circle
			msg.linear.x = 0.8
			msg.angular.z = 1.0
		elif self.time >= 54.5 and self.time < 57: #Second connection of inner circles
			msg.linear.x = 1.0
			msg.angular.z = 0.0
		else:		#done :)
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
