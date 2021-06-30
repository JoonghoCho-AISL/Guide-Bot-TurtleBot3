#!/usr/bin/env python



import rospy
from std_msgs.msg import String

def talker():
    pub=rospy.Publisher('distance',String,queue_size=10)
    rospy.init_node('dist_measurmetnt',anonymous=True)

    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        #dist = "10"
        send_str= 'dist = %s' % rospy.get_gime()
        rospy.loginfo(send_str)
        pub.publish(send_str)

        rate.sleep()

if __name__=='main':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



