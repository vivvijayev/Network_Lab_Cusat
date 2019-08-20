import socket

udp_ip ="127.0.0.1"
udp_port=5005
m="mia estavista"

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(m,(udp_ip,udp_port))
