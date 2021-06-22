# -- coding: utf-8 --
# echo_client.py
import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host, port))

ime = "ik"

while True:
    try:
        unos = input()
        if unos == ime:
            raise ValueError
    except ValueError:
        print('Unos nije podrzan!')
    else:
        break

print(unos)

client_socket.sendall("Hello World!!!".encode())

data = client_socket.recv(1024)

print(data)
print(datetime.datetime.now())
print_machine_info()

client_socket.close()
