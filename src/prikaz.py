#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(data):
    # Informacija o prosecnoj dnevnoj temperaturi
    avg_tmp = data.data
    # Ispis pristiglih informacija
    rospy.loginfo(rospy.get_caller_id() + ' Prosecna temperatura %f', avg_tmp)

def listener():
    # Inicijalizacija cvora 'Prikaz'
    rospy.init_node('Prikaz', anonymous=False)
    # Kreiranje subscriber objekta na topic 'prosecna_temperatura'
    rospy.Subscriber('prosecna_temperatura', Float32, callback)
    # Ponavljanje tela funkcije
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass