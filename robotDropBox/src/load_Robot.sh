rosservice call gazebo/delete_model dd_robot 
rosrun gazebo_ros spawn_model -sdf -file model.sdf -model dd_robot -y 0.0 -x 0.0 -z 1.0