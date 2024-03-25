#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def forward_motion():
    rospy.init_node('forward_motion', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Частота публикации команд (10 Гц)

    move_cmd = Twist()
    move_cmd.linear.x = 0.2  # Линейная скорость (0.2 м/с)
    
    while not rospy.is_shutdown():
        velocity_publisher.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        forward_motion()
    except rospy.ROSInterruptException:
        pass
