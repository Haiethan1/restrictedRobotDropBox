#! /usr/bin/env python
import rospy

from gazebo_msgs.srv import ApplyJointEffort


speed = 100

def setRot(pub, msg): 
    global speed
    d = msg 
    buff = ApplyJointEffort()

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)

    if (d != "increase" and d != "decrease"):
        if (d == "w"):
            pub("dd_robot::left_wheel_hinge", 1 * speed, start_time, end_time)
            pub("dd_robot::right_wheel_hinge",  1 * speed, start_time, end_time)
        elif (d == "s"):
            pub("dd_robot::left_wheel_hinge", -1 * speed, start_time, end_time)
            pub("dd_robot::right_wheel_hinge", -1 * speed, start_time, end_time)
        elif ( d == "d"):
            pub("dd_robot::left_wheel_hinge", 1 * speed, start_time, end_time)
            pub("dd_robot::right_wheel_hinge", -1 * speed, start_time, end_time)
        elif (d == "a"):
            pub("dd_robot::left_wheel_hinge", -1 * speed, start_time, end_time)
            pub("dd_robot::right_wheel_hinge", 1 * speed, start_time, end_time)
        else:
            pass
    else:
        if (d == "increase"):
            speed += 1
            print "Speed of robot = " + str(speed)
        else:
            if (speed >= 1):
                speed -= 1
                print "Speed of robot = " + str(speed)
            else:
                speed = 0
                print "Speed cannot be negative. Speed = 0"

rospy.init_node('keyboard', anonymous=True)
pub = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)

while(True):
    val = raw_input("Direction = ") #(if you want to speed up or down, type increase / decrease): 
    setRot(pub, val)



