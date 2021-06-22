# client_ssl.py

import socket
import ssl
import pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 10023))

print(repl(ssl_sock.getpeername()))
print(ssl_sock.cipher())
print(pprint.pformat(ssl_sock.getpeercert()))

ssl_sock.write("boo!")
