import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math
from alert import notify

def dataCollection():
   import time 
   UserEmails=[]
   username=raw_input("What is your username? ")
   password=raw_input("What is your password? ")

   try:
      savePath="/home/root/PlayersData"
      accountLocation= os.path.join(savePath, username+".txt")
      account=open(accountLocation, "a+")
   except IOError:
      print "No Account like %s /nPlease run the program again with a correct username."% username
   else:
      if password in account.readline():
         NameOfPlayer=username.split("_")[0]+" "+username.split("_")[1]
         print("Welcome User of "+NameOfPlayer)
         UserEmails=account.next()
         UserEmails=UserEmails.split(":")
         del UserEmails[0]

         SETTINGS_FILE = "RTIMULib"

         s = RTIMU.Settings(SETTINGS_FILE)
         imu = RTIMU.RTIMU(s)

         if (not imu.IMUInit()):
             sys.exit(1)

         # this is a good time to set any fusion parameters

         imu.setSlerpPower(0.02)
         imu.setGyroEnable(True)
         imu.setAccelEnable(True)
         imu.setCompassEnable(True)

         poll_interval = imu.IMUGetPollInterval()

         print("Starting Data Collection")

	 monitorTime=0
         Time=0.0

         while monitorTime<50:
	    monitorTime+=1
            Time+=0.1
            if imu.IMURead():                                        
               data = imu.getIMUData()                               
               accel = data["accel"]                                
               force = math.sqrt(accel[0]**2+accel[1]**2+accel[2]**2)
     	       #Time=time.asctime(time.localtime(time.time()))   
               print("%f g Time:%f" % (force, Time))                                    
               account.write("\n%f g Time:%f" % (force,Time) )
               #if force>10:
		 # Time=time.asctime(time.localtime(time.time()))                                          
         
                                            
               #   notify(UserEmails,NameOfPlayer,force)                
               time.sleep(0.1)
	       
                              
