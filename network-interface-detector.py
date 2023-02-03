# python3
from get_nic import getnic

print(getnic.interfaces())

interfaces = getnic.interfaces()
print(getnic.ipaddr(interfaces))
