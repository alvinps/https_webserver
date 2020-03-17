
from socket import *
import sys


clientSocket = socket(AF_INET, SOCK_STREAM)
Port_num = 8080
filename = "index.htm"
ip_address = str(sys.argv[1])
param_count  = len(sys.argv)
if param_count == 4:
    filename = str(sys.argv[3])
    Port_num = int(sys.argv[2])

elif param_count ==3:






serverSocket.bind(('',Port_num))
serverSocket.listen(Max_Connection_Allowed)
print("Connection ready on port %d...\n" % Port_num)
print("*** A Simple Web Server ***")

while True:
    #Establish the connection
    print("\n\n***************************************************************")
    print("Ready to serve...\n")
    connectionSocket, addr = serverSocket.accept()
    # print out details about the connection here.
    print("Connection Accepted by:\n")
    print("Client Host: %s" % gethostbyaddr(connectionSocket.getpeername()[0])[0])
    print("IP address: %s\nPort: %d" % connectionSocket.getpeername() )

    try:
        message = connectionSocket.recv(1024)
        print("\n\nMessage received: \n%s\n" % (message.decode("utf-8")))
        if message == '':
            print("Response sent: Bad Request 400")
            connectionSocket.send(bytes("HTTP/1.1 400 Bad Request\n","UTF-8"))
            connectionSocket.close()
        else:
            filename = message.split()[1]
            if filename == bytes("/","UTF-8"):
                filename = bytes("/index.htm","UTF-8")

            file = open(filename[1:])
            outputdata = file.read()
            print("Response sent: OK 200")
            connectionSocket.send(bytes("HTTP/1.1 200 OK\n","UTF-8"))
            print("File ( %s ) is being sent..." % (filename))
            for i in range(0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i],"UTF-8"))
    except IOError:
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n","UTF-8"))
        print("Response sent: File Not Found 404")

    connectionSocket.close()
    print("Closing connection... ")

serverSocket.close()
