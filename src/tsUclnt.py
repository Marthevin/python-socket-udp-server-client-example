from socket import *
from time import ctime

HOST = '100.69.33.71'
PORT = 23567
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpCliSock = socket(AF_INET,SOCK_DGRAM)

while True:
    sendData = raw_input("> ")
    if sendData is None:
        break
    udpCliSock.sendto(sendData,ADDR) 
    
    print "...waiting for response..."
    recv_data,ADDR = udpCliSock.recvfrom(BUFSIZE)
    if recv_data is not None:
       print "[%s]: receiving data from server %s:%s  :%s" %(ctime(),ADDR[0],ADDR[1],recv_data)
    
udpCliSock.close()