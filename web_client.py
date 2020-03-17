# WEB SERVER
# Alvin Poudel Sharma
# UTA ID: 1001555230

from socket import *
import sys
# socket and sys in modules imported

clientSocket = socket(AF_INET, SOCK_STREAM)
# default port number for connection if not provided.
Port_num = 8080
filename = "index.htm"
# default file name if no provided
ip_address = str(sys.argv[1])
param_count  = len(sys.argv)

# parameters received form the command line for the operation of the connection.
if param_count == 4:
    filename = str(sys.argv[3])
    Port_num = int(sys.argv[2])
elif param_count ==3:
    try:
        Port_num = int(sys.argv[2])
    except ValueError:
        filename = str(sys.argv[2])

# client connected to the server.
clientSocket.connect((ip_address, Port_num))
# client connection initiated to the server.
message ="GET /"+filename+" HTTP/1.1\n This came from the python client\n"
# message to be sent to the server.
clientSocket.send(bytes(message,"UTF-8"))
print("The following request was sent to the server: %s" % message)
print("Message Received: \n\n ")
while True:
    # response received from the server
    Response_received = clientSocket.recv(2048)
    if Response_received.decode("UTF-8") == "":
        break
    else:
        print("%s" % Response_received.decode("UTF-8"))

print("\nClosing connection...")
# connection closed.
clientSocket.close()
