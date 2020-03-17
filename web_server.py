# WEB SERVER
# Alvin Poudel Sharma
# UTA ID: 1001555230

from socket import *
import sys
import thread
# socket and sys in modules imported
Max_Connection_Allowed = 10

def new_connection(connectionSocket, addr):
    # print out details about the connection here.
    print("Connection Accepted by:\n")
    print("Client Host: %s" % gethostbyaddr(connectionSocket.getpeername()[0])[0])
    print("IP address: %s\nPort: %d" % connectionSocket.getpeername() )

    try:
        message = connectionSocket.recv(1024)
        # new message request received from client
        print("\n\nMessage received: \n%s\n" % (message.decode("utf-8")))
        if message == '':
            # if the message request is empty
            print("Response sent: Bad Request 400")
            connectionSocket.send(bytes("HTTP/1.1 400 Bad Request\n","UTF-8"))
        else:
            # if a file is requested by the client
            filename = message.split()[1]
            if filename == bytes("/","UTF-8"):
                filename = bytes("/index.htm","UTF-8")

            file = open(filename[1:])
            outputdata = file.read()
            print("Response sent: OK 200")
            connectionSocket.send(bytes("HTTP/1.1 200 OK","UTF-8"))
            print("File ( %s ) is being sent..." % (filename.decode("UTF-8")))
            for i in range(0, len(outputdata)):
                # sending all the data from the file to the client.
                connectionSocket.send(bytes(outputdata[i],"UTF-8"))
    except IOError:
        # if the file is not found then NOT FOUND is sent to the client
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\n","UTF-8"))
        print("Response sent: File Not Found 404")

    connectionSocket.close()
    # closing the connection
    print("Closing connection... ")

# server socket initiated
serverSocket = socket(AF_INET, SOCK_STREAM)
Port_num = 8080 # deafult port  number to be used
# if provided in the commandline that specific port number is used
if (len(sys.argv) >= 2):
    Port_num = int(sys.argv[1]) #

serverSocket.bind(('',Port_num))
# listening for a connection from a client
serverSocket.listen(Max_Connection_Allowed)
print("Connection ready on port %d...\n" % Port_num)
print("*** A Simple Web Server ***")

while True:
    #Establish the connection
    print("\n\n***************************************************************")
    print("Ready to serve...\n")
    connectionSocket, addr = serverSocket.accept() # new connection accepted
    thread.start_new_thread(new_connection,(connectionSocket,addr))

# closing the server
serverSocket.close()
