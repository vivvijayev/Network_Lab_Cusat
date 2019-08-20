import socket 

# Import hamming code check function from hamming code module
from hamming_code import checkHammingCode

# Creating Socket 
s = socket.socket() 
print ("Socket successfully created") 

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345

s.bind(('', port)) 
print ("socket binded to %s" % (port)) 
# put the socket into listening mode 
s.listen(5) 
print ("socket is listening") 


while True: 
	# Establish connection with client. 
	c, addr = s.accept() 
	print('Got connection from', addr) 
	
	# Get data from client 
	data = c.recv(1024) 

	print(data) 

	if not data: 
		break
	returnMessage = checkHammingCode(data)
	# TO MAKE ERROR USE THE NEXT LINE
	#returnMessage = checkHammingCode(data.replace('0','1',1))	
		 
	c.sendall(returnMessage) 
c.close() 
