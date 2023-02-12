import socket
import os
dns = input("Enter domain > ")
ip = socket.gethostbyname(dns)
print ("Site IP : ", ip)
print ("Do you want scan this ip?")
q = input("If you want enter yes > ")
if q == "yes" :
	os.system("python3 Scan\ IP.py")
input()
