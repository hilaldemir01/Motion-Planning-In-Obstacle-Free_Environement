#! /usr/bin/env python

# Hilal Demir
# 18070001020

import rospy
import sys
import random
import math

#chmod u+x ~/catkin_ws/src/try/src/midterm_turtles12.py

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

	# tihs method is used to change the position of the turtle's head in the direction of it's route

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

def t12rounds(num_unit):

	#this method is used for turtle to move as the sent parameter value

	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 0.0

	t0 = rospy.Time.now().to_sec()
	current_distance = 0
	
	while(current_distance < num_unit):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_distance = 0.1 * (t1-t0)
		rate.sleep()

	stop_motion()

def move_down():
	
	# This method is used to make it possible to go 0.3 unit down. This could be achieved by t12rounds() function too.

	distance = 0.3

	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 0.0

	t0 = rospy.Time.now().to_sec()
	current_distance = 0

	while(current_distance < distance):
		pub.publish(vel_msg)
		t1 = rospy.Time.now().to_sec()
		current_distance = 0.1 * (t1-t0)
		rate.sleep()

	stop_motion()

def decide_angle (flip_coin,before_movedown):

	# This method is used to decide whether which direction the turtle's head should be at.

	angle = 0
	if before_movedown == 0:
		if flip_coin == 0: #right
			angle = 0

		elif flip_coin == 1: #left
			angle = 180

	elif before_movedown == 1:
		if flip_coin == 0: #right
			angle = 91

		elif flip_coin == 1: #left
			angle = 271

	rospy.loginfo("Angle ="+ str(angle))
	return angle

def movetask():

	unit1 = 0# setting it initially to zero 
	unit2 = 0
	unit3 = 0

	# results of flipping coins area saved here

	flip_coin1 = random.randint(0,1) 
	flip_coin2 = random.randint(0,1)
	flip_coin3 = random.randint(0,1)

	# I just used them to debug the code while I was trying to solve how the pattern was going to look like

	rospy.loginfo("Flip1 ="+ str(flip_coin1))
	rospy.loginfo("Flip2 ="+ str(flip_coin2))
	rospy.loginfo("Flip3 ="+ str(flip_coin3))

# ----------------------------------------------------------------------------------------------------------------------
		# round 1:

# def t12rounds(is_return,num_unit, flip, pub, rate, vel_msg):
# def decide_angle (flip_coin, is_return, before_movedown):

	# calculating units :

	unit1 = 0.5

# ----------------------------------------------------------------------------------------------------------------------
		# round 2:

	if flip_coin1 == flip_coin2 :
		unit2 = unit1 + 0.1
	else :
		unit2 = unit1 * 2
	
# ----------------------------------------------------------------------------------------------------------------------
		# round 3:

	if flip_coin2 == flip_coin3 :
		unit3 = unit2 + 0.1
	else :
		unit3 = unit2 * 2

	# saving reverses of each flip_coins:

	if flip_coin1 == 0:
		reverse1 = 1
	elif flip_coin1 ==1:
		reverse1 = 0

	if flip_coin2 == 0:
		reverse2 = 1
	elif flip_coin2 ==1:
		reverse2 = 0

	if flip_coin3 == 0:
		reverse3 = 1
	elif flip_coin3 ==1:
		reverse3 = 0

	rospy.loginfo("Round1 =")
	change_direction(decide_angle(flip_coin1,0))
	t12rounds(unit1)
	change_direction(decide_angle(flip_coin1,1))
	move_down()
	change_direction(decide_angle(flip_coin1,1))
	t12rounds(unit1)

	rospy.loginfo("Round2 =")
	if flip_coin1 != flip_coin2:
		t12rounds(unit2)
		change_direction(decide_angle(flip_coin2,1))
		move_down()

	elif flip_coin1 == flip_coin2:
		change_direction(decide_angle(reverse1,1))
		move_down()
		change_direction(decide_angle(reverse2,1))
		t12rounds(unit2)

		change_direction(decide_angle(flip_coin2,1))
		move_down()

	change_direction(decide_angle(flip_coin2,1))
	t12rounds(unit2)


	rospy.loginfo("Round3 =")
	if flip_coin2 != flip_coin3:
		t12rounds(unit3)
		change_direction(decide_angle(flip_coin3,1))
		move_down()
		
	elif flip_coin2 == flip_coin3:
		change_direction(decide_angle(reverse2,1))
		move_down()
		change_direction(decide_angle(reverse3,1))
		t12rounds(unit3)

		change_direction(decide_angle(flip_coin3,1))
		move_down()

	change_direction(decide_angle(flip_coin3,1))
	t12rounds(unit3)
	
	stop_motion()

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
	try:
		movetask()
	except rospy.ROSInterruptException:
		pass


