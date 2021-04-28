#!/usr/bin/env python3

import rospy
import csv
from std_msgs.msg import String

csv_path = '/home/ros/Workspaces/getting_started/src/domaci_1/src/weather_data_nyc_centralpark_2016.csv'
last_row = 0 # Poslednji procitani red

def talker():
    global last_row
    # Kreiranje publisher objekta na topic 'temperature'
    pub = rospy.Publisher('temperature', String, queue_size=1)
    # Inicijalizacija cvora 'Merenja'
    rospy.init_node('Merenja', anonymous=False)
    # Rate = 10Hz
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        # Citanje .csv fajla
        with open(csv_path, 'r') as file:
            # Citanje sadrzaja fajla u listu redova
            rows = list(csv.reader(file))
            # Provera da li postoji red koji nije procitan
            if(last_row < len(rows)):
                # Citanje vrsti pocev od prve neprocitane
                last_row += 1
                for ind in range(last_row, len(rows)):
                    # Izdvajanje trenutne vrste
                    row = rows[ind]
                    # Provera trenutnog meseca
                    if(int(row[0].split('-')[1]) <= 7):
                        # Formiranje poruke u formatu 'maksimum,minimum,average_temperature'         
                        str = ",".join(row[1:4])
                        # Ispis poslate poruke
                        rospy.loginfo("date: " + row[0] + "\t Tmax, Tmin, Tavg = " + str)
                        # Slanje podataka
                        pub.publish(str)
                        # Pauza
                        r.sleep()
                # Poslednja procitana vrsta je poslednja vrsta u fajlu
                last_row = len(rows) - 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass