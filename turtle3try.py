#! /usr/bin/env python

# Hilal Demir
# 18070001020 
import rospy
import sys
import random
import math

#chmod u+x ~/catkin_ws/src/try/src/midterm_turtle3.py

from geometry_msgs.msg import Twist

nodeid= str(sys.argv[1])
nodename='turtle'+nodeid
rospy.init_node('movenode',anonymous=True)
pub = rospy.Publisher('/'+nodename+'/cmd_vel', Twist, queue_size = 10)

vel_msg = Twist()

rate=rospy.Rate(10)
rospy.loginfo("Moving...")

def stop_motion():

	# this method is to stop all motion 

	vel_msg.linear.x= 0.0
	vel_msg.linear.y= 0.0
	vel_msg.linear.z= 0.0
	vel_msg.angular.x= 0.0
	vel_msg.angular.y= 0.0
	vel_msg.angular.z= 0.0
	pub.publish(vel_msg)

def change_direction(angle):

	# this method is used to change the turtle's head position at the initial round

	speed = 10.0
	lspeed = 0
	clockwise = -1

	rospy.loginfo("Rotating...")
	
	angularspeed = speed * (math.pi/180)
	relativeangle = angle * (math.pi/180)

	vel_msg.linear.x=lspeed
	vel_msg.angular.z=clockwise * angularspeed
	
	t0=rospy.Time.now().to_sec()
	current_angle=0
	
	while(current_angle < relativeangle):
		pub.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		current_angle= angularspeed * (t1-t0)
		rate.sleep()

	stop_motion()

def t3round(radius,flip,clockwise):

	#this method is used to take the route of the turtle for a round
	speed = 5.0

	angle = 180
	rospy.loginfo("Rotating...")
	angularspeed = speed * (math.pi/180)
	relativeangle = angle * (math.pi/180)
	lspeed = angularspeed * radius

	vel_msg.linear.x=lspeed
	vel_msg.angular.z=clockwise * angularspeed
	
	vel_msg.linear.x = vel_msg.linear.x
	vel_msg.angular.z = vel_msg.angular.z

	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	
	t0=rospy.Time.now().to_sec()
	current_angle=0
	
	while(current_angle < relativeangle):
		pub.publish(vel_msg)
		t1=rospy.Time.now().to_sec()
		current_angle= angularspeed * (t1-t0)
		rate.sleep()
		
	stop_motion()
	pub.publish(vel_msg)


def movetask():

	# flipping coins and saving their results

	flip_coin1 = random.randint(0,1) 
	flip_coin2 = random.randint(0,1)

# ----------------------------------------------------------------------------------------------------------------------


# def t12rounds(is_return,num_unit, flip, pub, rate, vel_msg):
# def decide_angle (flip_coin, is_return, before_movedown):

	radius1 = 0.5 #initial radius
# ----------------------------------------------------------------------------------------------------------------------

	#radius calculation according to flip result sequence
	if flip_coin1 == flip_coin2 :
		radius2 = radius1 + 0.1
	else :
		radius2 = radius1 * 2

# ----------------------------------------------------------------------------------------------------------------------
	#deciding the turtle's head position and clockwise for the first round
	
	if flip_coin1 == 0:
		clockwise = -1
		change_direction(1)
	elif flip_coin1 == 1:
		change_direction(179)
		clockwise = 1
	#deciding the turtle's clockwise for the second round

	t3round(radius1,flip_coin1,clockwise)

	if flip_coin1 == flip_coin2 :
		#change_direction(181)
		clockwise = -1
	elif flip_coin1 != flip_coin2:
		#change_direction(2)
		clockwise = 1
	t3round(radius2,flip_coin2,clockwise)
# ----------------------------------------------------------------------------------------------------------------------
	# the end
	stop_motion()


if __name__ == "__main__":
	try:
		movetask()
	except rospy.ROSInterruptException:
		pass


