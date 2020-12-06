import socket
import os
from requests import get

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
gw = os.popen("ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
gateway = gw[2]
host = socket.gethostname()
public_ip = get ('https://api.ipify.org').text
print("")
print(f" \033[1;93mHostname:  \033[1;34m{hostname}")
print(f" \033[1;93mLocal IP:  \033[1;36m{local_ip}")
print(f" \033[1;93mYour IP:   \033[1;92m{ipaddr}")
print(f" \033[1;93mPublic IP: \033[1;91m{public_ip}")
print("")
print("   \033[1;37mBy \033[1;36mNet\033[1;91mcat")
print("")
