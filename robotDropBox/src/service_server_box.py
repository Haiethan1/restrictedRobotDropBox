#! /usr/bin/env python
import rospy
from std_srvs.srv import Trigger, TriggerResponse

import os
import time as t
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
import numpy



name = 'box'
box_i = 0

robot_proxy = None 



def trigger_response(request):
    global box_i
    dropBoxBool = False
    a = getRobotLocation()
    x = a[0]
    y = a[1]

    b = getBoxLocation(x, y) 
    if(b != None):
        dropBox(b[0], b[1])
        dropBoxBool = True

    return TriggerResponse(
        success=dropBoxBool,
        message="ooo"
    )



def dropBox(x, y):
    b0 = "./load_box.sh "
    b1 = name + str(box_i) + " "
    box_i += 1

    b2 = str(x) + " "
    b3 = str(y) + " "
    b4 = "&"

    buff = b0 + b1 + b2 + b3 + b4

    os.system(buff)


def getBoxLocation(x , y):
    
    # math for circle
    # determine if it is inside of the 50m - 2m circle (for our proj, square)
    x0 = 0.0
    y0 = 0.0
    dist = ((x-x0)^2 + (y-y0)^2)^0.5
    
    if (dist < 48):
        return None
    else:
        return #position

    return



def getRobotLocation():
    a = GetModelStateRequest(model_name = 'dd_robot')
    
    s = robot_proxy(a)

    print s

    x = s.pose.position.x
    y = s.pose.position.y

    return (x, y)



rospy.init_node('service_example')
my_service = rospy.Service(
    '/service_example_topic', Trigger, trigger_response
)

robot_proxy = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)


rospy.spin()