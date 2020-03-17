# https_webserver
A multi threaded web server using HTTP protocol

Written in:    Python 3

Description:
This is a simple multi threaded web server that uses HTTP protocol to handle a
simple GET request from any client and processes it and send the respective file
to the client. It can also have multiple connection with clients creating
a workable connection.

Execution Procedure:

Please make sure all the files are in the same directory and make sure it the
current working directory.

web_server.py :
In order to execute the server, type

                  python3 web_server.py <port_number>

                  python3 web_server.py 5644
  or,          
                  python3 web_server.py

please note the second argument is port number and is optional. It is used for
the opening the connection and will be set to 8080 if no port is specified


web_client.py:
In order to execute the client, type
                  python3 web_client.py <ip_address> <port number> <file>
  Eg,
                  python3 web_client.py localhost 5644 test.html
  or,
                  python3 web_client.py localhost test.html
  or,
                  python3 web_client.py localhost


please note the port number and file name is optional. If not provided a default
port number of 8080 will be used and default of index.htm will be used.

Resources Used:
-> Socket Programming https://docs.python.org/3/howto/sockets.html
->
