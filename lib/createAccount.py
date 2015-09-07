import time
import math
import os.path
import math
import os.path

def createAccount():
   numberOfUsers=1
   answer2=False
   users=[]
   playerFirstName=raw_input("What is your player's first name? ")
   playerLastName=raw_input("What is your player's last name? ")
   playerName=playerFirstName+"_"+playerLastName
   raw_input("Here is your Username: "+playerName+"\nPress Enter to continue...")

   savePath="/home/root/PlayersData"
   accountLocation= os.path.join(savePath, playerName+".txt")
   account=open(accountLocation, "w")

   while answer2==False:
      password=raw_input("Enter a password for your Account: ")
      password_verification=raw_input("Confirm your password: ")
      if password_verification == password:
         answer2=True

   newUser=raw_input("Enter the primary email: ")
   users.append(newUser)
   answer1=raw_input("Do you want to add another email? (Y/N):")

   while answer1=="Y":
      newUser=raw_input("Enter the email: ")
      users.append(newUser)
      numberOfUsers+=1
      answer1=raw_input("Do you want to add another email? (Y/N):")

   account.write("Password:"+password+"\nEmails:")
   for i in range(numberOfUsers):
      if i != (numberOfUsers-1):
         account.write(users[i]+":")
      else:
         account.write(users[i])
   
