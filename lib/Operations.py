import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
from alert import notify

SETTINGS_FILE = "RTIMULib"

print("Using settings file " + SETTINGS_FILE + ".ini")
if not os.path.exists(SETTINGS_FILE + ".ini"):
  print("Settings file does not exist, will be created")

s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

print("IMU Name: " + imu.IMUName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded")

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

answer="Y"
users=[]
playerName=raw_input("What is your player's name? ")

while answer=="Y":
   newUser=raw_input("Enter the email of the user: ")
   users.append(newUser)
   answer=raw_input("Do you want to add another user? (Y/N):")
while True:
   if imu.IMURead():                                        
      data = imu.getIMUData()                               
      accel = data["accel"]                                
      force = math.sqrt(accel[0]**2+accel[1]**2+accel[2]**2)
      if force>10:                                          
         print("Force: %f" % force)                         
         notify(users,playerName,force)                
      time.sleep(poll_interval*1.0/1000.0)

