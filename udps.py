import socket
udp_ip="127.0.0.1"
udp_port= 5005

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((udp_ip,udp_port))

while True:
	data,addr = s.recvfrom(15)
	print "recieved:",data 
