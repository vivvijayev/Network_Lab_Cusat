import socket

s=socket.socket()
print("socket set")
port=17879

s.bind(('127.0.0.1',port))
print "binded %s" %port

s.listen(15)

while True:
	k,a=s.accept()
	print "connected to",a
	k.send("mia estavista")
	k.close()
