#!/usr/bin/env python
import rospy
from common_msgs.msg import cm
from common_msgs.srv import AddTwoNum, AddTwoNumResponse

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.point.x, msg.point.y, msg.point.z

rospy.init_node('algorithm_subscriber')
sub = rospy.Subscriber('sensor_msg', cm, callback)

def service_callback(request):
    response = cmResponse(sum=request.a + request.b)
    print "request data:", request.a, request.b, ", response:", response.sum
    return response

rospy.init_node('service_server')
service = rospy.Service('add_two_number', AddTwoNum, service_callback)

rospy.spin()
