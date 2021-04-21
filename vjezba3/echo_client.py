# echo_client.py

from local_machine_info import print_machine_info
import socket
import datetime
print(datetime.datetime.now())


print_machine_info()

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host, port))

client_socket.sendall('Dobar dan serveree'.encode())

unos = input("Unesite neku recenicu")
print(unos)

data = client_socket.recv(1024)

print(data)
client_socket.close()
