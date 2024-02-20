#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

# Parameter for Defult Scale
#
#

frame = Tk()
frame.title("REMOTE")
frame.geometry("200x300")

# Initial ROS node and determine Publish or Subscribe action
#
#
#
rospy.init_node("Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)
pub_text = rospy.Publisher("chatter",String,queue_size=10)

def fw():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Forword")
        
def bw():
    cmd = Twist()
    cmd.linear.x = -LinearVel.get()
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("Backword")
       
def lt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= AngularVel.get()
    #publish
    pub.publish(cmd)
    pub_text.publish("Turn left")
   
def rt():
    cmd = Twist()
    cmd.linear.x = LinearVel.get()
    cmd.angular.z= -AngularVel.get()
    #publish
    pub.publish(cmd)
    pub_text.publish("Turn right")
    
def pn():
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z= 1.0
    #publish
    pub.publish(cmd)
    pub_text.publish("PenOn")
    
def po():
    cmd = Twist()
    cmd.linear.x = 0.0
    cmd.angular.z= 0.0
    #publish
    pub.publish(cmd)
    pub_text.publish("PenOff")
    
LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
LinearVel.set(1) # 1 is defult value for scale
LinearVel.pack()

AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
AngularVel.set(1) # 1 is defult value for scale
AngularVel.pack()

B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=120)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=230)

B3 = Button(text = "LT", command=lt)
B3.place(x=20, y=180)

B4 = Button(text = "RT", command=rt)
B4.place(x=128, y=180)

B5 = Button(text = "pn", command=pn)
B5.place(x=200, y=180)

B6 = Button(text = "po", command=po)
B6.place(x=200, y=250)


frame.mainloop()   
