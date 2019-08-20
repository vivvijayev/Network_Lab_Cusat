import socket			

# Import hamming code generator from hamming code module
from hamming_code import genHammingCode

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345			

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

input_string = raw_input("Enter data you want to send->") 
#s.sendall(input_string) 
data = list(input_string) 
print(data) 
ans = genHammingCode(data) 
print('sending hamming code of data: ',ans) 
s.sendall(str(ans)) 


# receive data from the server 
print(s.recv(1024)) 

# close the connection 
s.close() 

