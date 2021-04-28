#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

brojac = 0

def callback(data):
    global brojac
    # Ukoliko su oscilacije velike, brojac se inkrementira
    if data.data:
        brojac += 1
    # Ispis dobijenih informacija
    rospy.loginfo(rospy.get_caller_id() + ' Oscilacije su %s, brojac = %d', "velike" if data.data else "male", brojac)


def listener():
    # Inicijalizacija cvora 'Akcija'
    rospy.init_node('Akcija', anonymous=False)
    # Kreiranje subscriber objekta na topic 'komanda_akcije'
    rospy.Subscriber('komanda_akcije', Bool, callback)
    # Ponavljanje tela funkcije
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass