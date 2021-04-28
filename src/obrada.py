#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32, String, Bool

pub_prikaz = rospy.Publisher('prosecna_temperatura', Float32, queue_size=1)
pub_akcija = rospy.Publisher('komanda_akcije', Bool, queue_size=1)

def F2C(fahrenheit):
    return (float(fahrenheit) - 32)/1.8

def callback(data):
    # Ispis o prijemu informacija
    rospy.loginfo(rospy.get_caller_id() + ' Tmax, Tmin, Tavg = %s', data.data)
    # Konverzija primljenih informacija o temperaturi u float i F -> C
    max_tmp, min_tmp, avg_tmp = [float(F2C(T)) for T in data.data.split(',')]

    # Slanje informacija o prosecnoj temperaturi
    pub_prikaz.publish(avg_tmp)

    # Slanje komande za akciju
    command = False
    if (max_tmp - min_tmp) > 15:
        command = True
    pub_akcija.publish(command)

def listener():
    # Inicijalizacija cvora Obrada
    rospy.init_node('Obrada', anonymous=False)
    # Kreiranje subscriber objekta na topic 'temperature'
    rospy.Subscriber('temperature', String, callback)
    # Ponavljanje tela funkcije
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass