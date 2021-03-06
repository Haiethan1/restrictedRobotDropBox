import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.srv import GetModelState




rospy.init_node('bounds_check', anonymous=True)
pub = rospy.Publisher('/box', Twist, queue_size=10)

# robot moves max 10m/sec
V_max = .5 # m/s
L_buff = 2 # buffer room
h_box = 5 # m box drop height
t_ground = 1.01 # sec (based on a height of 5m)
T = 0.02 # sampling rate
t_loading = 1.5 # time for loading

t_for_bugger = L_buff/V_max
d_from_v_max_to_ground = V_max * t_ground # m - 10.1m
d_from_sampling = V_max * T # m - 1m
d_from_loading = V_max * t_loading
d_total = d_from_sampling + d_from_v_max_to_ground + d_from_loading

print("dist from T %f" %(d_from_sampling))
print("dist from Box %f" %(d_from_v_max_to_ground))
print("dist from loading %f" %(d_from_loading))
print(d_total)


def handle_setBox(req):
    #TODO: Spawn box
    print(req)




s = rospy.Service('/box', Twist, handle_setBox)



