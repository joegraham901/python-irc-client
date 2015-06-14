__author__ = 'Don'

import socket



# connection function
def connect(target_server, port):
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    socketaddrraw = socket.getaddrinfo(target_server, port)
    socketaddrtuple = socketaddrraw[0]
    socketaddr = socketaddrtuple[4]
    try:
        s.connect(socketaddr)
    except socket.error as exception:
        print 'fuck errors'  #this is why you sanitize source code
        s.close()
        return "Failed to connect: " + exception.message
    return s