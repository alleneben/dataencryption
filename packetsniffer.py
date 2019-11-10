import socket, sys
from struct import *


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

except socket.error, msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


while True:
    packet = s.recvfrom(65565)
    # packet = packet[0]

    print packet