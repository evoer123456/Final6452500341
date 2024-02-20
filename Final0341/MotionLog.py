#!/usr/bin/env python3
from tkinter import *
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from subprocess import call

root = Tk()
root.geometry("300x300")
root.title(" Show Action ")

def clearToTextInput():
	ActOut.delete("1.0","end")
	call(["rosservice", "call", "/reset"])

def run(val):
	ActOut.insert(END, val.data + "\n")

if __name__ == "__main__":
	#  Initial ROS node and determine Publish or Subscribe action	
	rospy.init_node("Motion")
	sub = rospy.Subscriber("chatter",String,callback=run)

	ActLabel = Label(text = "Motion", font = ("",18))
	ActLabel.place(x=113, y=10)
	ActOut = Text(root, height = 7, width = 10, bg = "light cyan", font = ("",16))
	ActOut.place(x=83, y=50)

	ClearBtn=Button(root,height=1,width=10,text="Clear",command=clearToTextInput)
	ClearBtn.place(x=103, y=250)
	

	mainloop()
