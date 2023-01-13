#! /usr/bin/env python

import sys
from nav_msgs.srv import GetMap, GetMapRequest
import rospy

rospy.init_node('get_map_node')
rospy.wait_for_service('/static_map')
get_map_service = rospy.ServiceProxy('/static_map', GetMap)
get_map_object = GetMapRequest()
result = get_map_service(get_map_object)
print(result)
