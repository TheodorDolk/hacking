# step 1

import sys
import socket
cmd_args = sys.argv
IP = cmd_args[1]
port = int(cmd_args[2])
msg = cmd_args[3]
msg_byte = msg.encode()

address = (IP, port)
with socket.socket() as client_socket:
    client_socket.connect(address)
    client_socket.send(msg_byte)
    response_byte = client_socket.recv(1024)
response = response_byte.decode()
print(response)



