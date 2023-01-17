#! /usr/bin/env python

import sys
import rospy

from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import PoseWithCovarianceStamped


def callback(msg):
    print(msg.pose)


def service_callback(request):
    sub = rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, callback)
    return EmptyResponse()


rospy.init_node('get_pose_node')
rospy.Service('/my_amcl_pose', Empty, service_callback)
rospy.spin()
