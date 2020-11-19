#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from common_msgs.msg import cm
from common_msgs.srv import cm, cmRequest

rospy.init_node('sensor_publisher')
pub = rospy.Publisher('sensor_msg', cm, queue_size=1)
msg = cm()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.point = Point(x=second%4, y=second%7, theta=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z
    rate.sleep()

rospy.init_node('service_client')
rospy.wait_for_service('add_two_number')
requester = rospy.ServiceProxy('add_two_number', cm)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 100:
    if count % 10 == 0:
        req = cmRequest(a=count, b=count/2)
        res = requester(req)
        print count, "request:", req.a, req.b, "response:", res.sum
    rate.sleep()
    count += 1
