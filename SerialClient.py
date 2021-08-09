#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg._PoseStamped import PoseStamped
import serial

def euler_to_quaternion(yaw, pitch, roll):

    qx = np.sin(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) - np.cos(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)
    qy = np.cos(roll/2) * np.sin(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.cos(pitch/2) * np.sin(yaw/2)
    qz = np.cos(roll/2) * np.cos(pitch/2) * np.sin(yaw/2) - np.sin(roll/2) * np.sin(pitch/2) * np.cos(yaw/2)
    qw = np.cos(roll/2) * np.cos(pitch/2) * np.cos(yaw/2) + np.sin(roll/2) * np.sin(pitch/2) * np.sin(yaw/2)

    return [qx, qy, qz, qw]

def talker():
    ser = serial.Serial('/dev/ttyACM7', 9600)

    pub = rospy.Publisher('SensorPose', PoseStamped, queue_size=45)
    rospy.init_node('talker')
   # print('hello')
    while not rospy.is_shutdown():
      # print('hi')
       data = ser.readline()
       dataString = str(data)
       splitCheck = dataString.split('Gyro: ')
      # print('hello back')
       try:
            
            newString = splitCheck[1].split(', ')
            
            #pub.publish(dataString)
            #print(len(newString))
            if len(newString)==3:
                try:
                    quaternion = euler_to_quaternion(float(newString[2]),float(newString[1]),float(newString[0]))
                    sensor = PoseStamped()
                    sensor.header.seq = 1
                    sensor.header.stamp = rospy.Time.now()
                    sensor.header.frame_id = "map"
                    sensor.pose.position.x = 0
                    sensor.pose.position.y = 0
                    sensor.pose.position.z = 0
                    sensor.pose.orientation.x = quaternion[0]
                    sensor.pose.orientation.y = quaternion[1]
                    sensor.pose.orientation.z = quaternion[2]
                    sensor.pose.orientation.w = quaternion[3]
                    rospy.loginfo(sensor)
                    pub.publish(sensor)
                    rospy.sleep(.001)
                    
                except ValueError:
                    pass
            else:
                pass
       except IndexError:
          #  newString = splitCheck[1].split(', ')
            pass

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass