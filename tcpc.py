import socket
s=socket.socket()
port=17879
s.connect(('127.0.0.1',port))
print(s.recv(15))
s.close
