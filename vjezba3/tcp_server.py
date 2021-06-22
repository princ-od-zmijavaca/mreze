# tcp_server.py

import socket

server_socket = socket.socket()
host = socket.gethostname()
port = 9999

server_socket.bind((host, port))
print(host, port, server_socket)

print("Waiting for connection...")
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    print('Got Connection from', addr)
    conn.send('Ivan Pelivan je gej' .encode())
    conn.close()
