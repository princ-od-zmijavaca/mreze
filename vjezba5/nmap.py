
# -*- coding: UTF-8 -*-

import socket
import datetime
from local_machine_info import print_machine_info
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Vrijeme pokretanja programa: ', datetime.datetime.now())
print('Program se izvodi na ovom racunalu: ')
print_machine_info()

print('--------------------------------------------------------------')

hostAddress = "www.aspira.hr"
ipAddress = socket.gethostbyname(hostAddress)
print('Skeniram host: ', hostAddress, ' IP adresa: ', ipAddress)

portNum1 = int(input('Pocetni port >> '))
portNum2 = int(input('Zavrsni port >> '))


def scanner(port):
    try:
        sk.connect((hostAddress, port))
        return True
    except:
        return False


for portNumber in range(portNum1, portNum2):
    print("Skeniram port: ", portNumber)
    if scanner(portNumber):
        print('Port', portNumber, 'je otvoren')

print('Skeniranje portova zavrseno!!!')
