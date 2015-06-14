__author__ = 'Don'

import clientfunctions, threading, sys

if len(sys.argv) < 1:
    print "usage: python clientmain.py username@server_address[:port]"

else:
    args = sys.argv[0].split("@")
    if args.__contains__(":"):
        user = args[0]
        serverHandle = args[1].split(":")
        host = serverHandle[0]
        port = serverHandle[1]
    else:
        user = args[0]
        host = args[1]
        port = 6667

#host = raw_input('What is the host? ')
#port = raw_input('What is the port? ')

conversationSocket = clientfunctions.connect(host, port)

while True:
    message = raw_input("IRC>")
    conversationSocket.sendall(message)
