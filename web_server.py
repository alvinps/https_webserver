
from socket import *
import sys
Max_Connection_Allowed = 10

serverSocket = socket(AF_INET, SOCK_STREAM)
Port_num = 8080
if (len(sys.argv) >= 2):
    Port_num = int(sys.argv[1])
print(Port_num)
print("TEst")

serverSocket.bind(('',Port_num))
serverSocket.listen(Max_Connection_Allowed)

while True:
    #Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    # print out details about the connection here.
    #Fill in start
    #Fill in end
    filename = ""
    try:
        message = connectionSocket.recv(1024)
        if message != '':
            filename = message.split()[1]

        filename = message.split()[1]
        try:
            file = open(filename[1:])
            outputdata = file.read()
            connectionSocket.send(bytes("HTTP/1.1 200 OK\n","UTF-8"))
            for i in range(0, len(outputdata)):
                connectionSocket.send(bytes(outputdata[i],"UTF-8"))
            connectionSocket.close()
        except IOError:
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n","UTF-8"))
            connectionSocket.close()
    except RuntimeError:
        connectionSocket.send(bytes("HTTP/1.1 400 Bad Request\n","UTF-8"))
    connectionSocket.close()

serverSocket.close()
