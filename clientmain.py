__author__ = 'Don'

import clientfunctions

host = raw_input('What is the host? ')
port = raw_input('What is the port? ')

clientfunctions.connect(host, port)
