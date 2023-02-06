# python3
# it only works on linux!!
from get_nic import getnic

print(getnic.interfaces())

interfaces = getnic.interfaces()
print(getnic.ipaddr(interfaces))
