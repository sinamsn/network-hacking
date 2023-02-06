# python3
# it only works on linux!!
from get_nic import getnic
import netifaces as ni

print("all your interfaces...")
for interface in getnic.interfaces():
	print(interface)


print("-------------")
try:
	for interface in getnic.interfaces():
		print("interface "+interface+" ip: "+ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
		#print(ni.ifaddresses(interface)[ni.AF_INET][0]['addr'])
except:
	print("interface "+ interface+" has no ip !!")
