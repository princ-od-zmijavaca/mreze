# tcp_client.py
import socket
client_socket = socket.socket()
host = socket.gethostname("www.google.hr")
port = 9999

client_socket.connect((host, port))
print(client_socket.recv(1024))

client_socket.close()
