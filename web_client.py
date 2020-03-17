
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
    try:
        Port_num = int(sys.argv[2])
    except ValueError:
        filename = str(sys.argv[2])


clientSocket.connect((ip_address, Port_num))
message ="GET /"+filename+" HTTP/1.1\n This came from the python client\n"
clientSocket.send(bytes(message,"UTF-8"))
print("The following request was sent to the server: %s" % message)
print("Message Received: \n\n ")
while True:
    Response_received = clientSocket.recv(2048)
    if Response_received.decode("UTF-8") == "":
        break
    else:
        print("%s" % Response_received.decode("UTF-8"))

print("\nClosing connection...")
clientSocket.close()
