#-----------print python version 
import sys
print("Python Version :")
print(sys.version)
# print("Python Version Info:")
# print(sys.version_info)



#-----------print Current Date Time 
import datetime
now = datetime.datetime.now()
print(now)
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))