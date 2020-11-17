#!/usr/bin/env python
import rospy
from common_msgs.msg import cm

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.theta

rospy.init_node('ag_subscriber')
sub = rospy.Subscriber('custom_msg', cm, callback)
rospy.spin()
