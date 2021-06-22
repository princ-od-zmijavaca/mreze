# gugl.py

import socket

client_socket = socket.socket()
host = socket.gethostbyname("www.google.hr")
port = 80

client_socket.connect((host, port))
print("The socket has successfully connected to Google on port == ",
      port, ", and IP adress == ", host)

client_socket.close()
