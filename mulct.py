import socket, select, string, sys


def display() :
	you=""+" You: "+""
	sys.stdout.write(you)
	sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        host = raw_input("Enter host ip address: ")
    else:
        host = sys.argv[1]

    port = 5256
    
    
    name=raw_input(" CREATING NEW ID:\n Enter username: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    
   
    try :
        s.connect((host, port))
    except :
        print " Can't connect to the server \n"
        sys.exit()

    
    s.send(name)
    display()
    while 1:
        socket_list = [sys.stdin, s]
        
        
        rList, wList, error_list = select.select(socket_list , [], [])
        
        for sock in rList:
           
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print ' DISCONNECTED!!\n'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    display()
        
            else :
                msg=sys.stdin.readline()
                s.send(msg)
                display()

if __name__ == "__main__":
    main()
