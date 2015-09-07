import sys
from lib.ForceFusion import collectData
from lib.createAccount import createAccount
from lib.DataCollection import dataCollection

print("What would you like to do?")
print("1) Collect Data?")
print("2) Create an Account?")
print("3) Data Collection")
answer=int(raw_input("Enter the number that is associated with what you want to do: "))


if answer==1:
   collectData()
if answer==2:
   createAccount()
if answer==3:
   dataCollection() 
