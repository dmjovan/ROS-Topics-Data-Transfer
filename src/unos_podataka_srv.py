#!/usr/bin/env python3

import rospy
from ROS_Topics_Data_Transfer.srv import unos_podataka, unos_podatakaResponse

csv_path = '/home/ros/Workspaces/getting_started/src/domaci_1/src/weather_data_nyc_centralpark_2016.csv'

# Funkcija za konverziju unetih podataka iz Celzijusove u Farenhajtovu skalu
def C2F(celsius):
    return str(float(celsius)*1.8 + 32)


def response_callback(req):
    # Kreiranje nove vrste u .csv fajlu
    new_row = "xx-0-xxxx,"+C2F(req.Tmax)+","+C2F(req.Tmin)+","+C2F(req.Tavg)+",NaN,NaN,NaN\n"
    # Upis nove vrste u fajl
    file = open(csv_path, 'a+')
    file.write(new_row)
    file.close()
    # Ispis dodatih podataka u fajl
    rospy.loginfo(new_row)
    # Povratna vrednost servisa
    return unos_podatakaResponse(True)

rospy.init_node('unos_podataka_u_csv')
s = rospy.Service('unos_podataka', unos_podataka, response_callback)
rospy.loginfo("Servis za unos podataka je spreman!")
rospy.spin()