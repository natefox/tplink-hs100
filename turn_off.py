#!/usr/bin/python

import socket

IPADDR = '192.168.1.150'
PORTNUM = 9999

# FROM ON TO OFF
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDR, PORTNUM))
data = '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedea3dea3'.decode('hex')
s.send(data)
data = '0000002dd0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381e496e4bbd8b7d3b694ae9ee39ee3'.decode('hex')
s.send(data)
s.close

