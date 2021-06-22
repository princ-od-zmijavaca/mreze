from socket import SOCK_DGRAM, socket

s = socket(type=SOCK_DGRAM)
s.sendto('SRECNA NOVA GODINA', ('localhost', 5000))
data, addr = s.recvfrom(1024)
print(data, addr)
