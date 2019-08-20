import socket, select


def send_to_all (sock, message):
	
	for socket in connected_list:
		if socket != server_socket and socket != sock :
			try :
				socket.send(message)
			except :
				
				socket.close()
				connected_list.remove(socket)

if __name__ == "__main__":
	name=""
	
	record={}
	
	connected_list = []
	buffer = 4096
	port = 5256

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_socket.bind(("localhost", port))
	server_socket.listen(10) 

	
	connected_list.append(server_socket)

	print "\t\t\tSERVER WORKING" 

	while 1:
        
		rList,wList,error_sockets = select.select(connected_list,[],[])

		for sock in rList:
			
			if sock == server_socket:
				
				sockfd, addr = server_socket.accept()
				name=sockfd.recv(buffer)
				connected_list.append(sockfd)
				record[addr]=""
				
                
                
				if name in record.values():
					sockfd.send("Username already taken!")
					del record[addr]
					connected_list.remove(sockfd)
					sockfd.close()
					continue
				else:
                   
					record[addr]=name
					print "Client (%s, %s) connected" % addr," [",record[addr],"]"
					sockfd.send(" Welcome to chat room. Enter 'tata' anytime to exit\n")
					send_to_all(sockfd, " "+name+" joined the conversation \n")

			
			else:
				
				try:
					data1 = sock.recv(buffer)
					
					data=data1[:data1.index("\n")]
					
                    
                   
					i,p=sock.getpeername()
					if data == "tata":
						msg=" "+record[(i,p)]+" left the conversation \n"
						send_to_all(sock,msg)
						print "Client (%s, %s) is offline" % (i,p)," [",record[(i,p)],"]"
						del record[(i,p)]
						connected_list.remove(sock)
						sock.close()
						continue

					else:
						msg=" "+record[(i,p)]+": "+""+data+"\n"
						send_to_all(sock,msg)
            
              
				except:
					(i,p)=sock.getpeername()
					send_to_all(sock, ""+record[(i,p)]+" left the conversation unexpectedly\n")
					print "Client (%s, %s) is offline (error)" % (i,p)," [",record[(i,p)],"]\n"
					del record[(i,p)]
					connected_list.remove(sock)
					sock.close()
					continue

	server_socket.close()

