#! /usr/bin/env/python

import sys
from std_srvs.srv import Empty, EmptyRequest
import rospy

rospy.init_node('service_client')
rospy.wait_for_service('/global_localization')
global_loc_service = rospy.ServiceProxy('/global_localization', Empty)
global_loc_object = EmptyRequest()
result = global_loc_service(global_loc_object)
