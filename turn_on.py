#!/usr/bin/python

import socket
import time

IPADDR = '192.168.1.150'
PORTNUM = 9999

## FROM OFF TO ON
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDR, PORTNUM))
data = '0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedfa2dfa2'.decode('hex')
s.send(data)

## seems to need to pause for a moment. I havent tried turning this down to less than 1s
time.sleep(1)

data = '00000025d0f281e28aef8bfe92f7d5ef94b6d1b4c09ff194ec98c7a6c5b1d8b7d9fbc1afdab6daa7da'.decode('hex')
s.send(data)
s.close()

