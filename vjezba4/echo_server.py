# -- coding: utf-8 --
# echo_server.py

from local_machine_info import *

import socket
import datetime

host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host, port))
echo_server.listen(5)


print("Cekam klijenta...")
print_machine_info()
conn, addr = echo_server.accept()

print("Spojen ", addr)

echo_server.listen(5)
while True:
    data = conn.recv(1024)
    if not data:
        break
conn.sendall(data)

print(datetime.datetime.now())

conn.close()
