# step 3
import itertools
import sys
import socket

cmd_args = sys.argv
IP = cmd_args[1]
port = int(cmd_args[2])
address = (IP, port)

with socket.socket() as client_socket:
    client_socket.connect(address)
    with open(
            r"C:\Users\theod\PycharmProjects\Password Hacker (Python)1\Password Hacker (Python)\task\hacking\passwords.txt",
            "r") as passwords_file:
        for password in passwords_file:
            # remove newline character
            password = password[:-1]
            for bit_pattern in itertools.product([0, 1], repeat=len(password)):
                combination = ''.join(char.upper() if bit else char for char, bit in zip(password, bit_pattern))
                password_byte = combination.encode()
                client_socket.send(password_byte)
                response_byte = client_socket.recv(1024)
                response = response_byte.decode()
                if response == "Connection success!":
                    print(combination)
                    exit()
                if response == "Too many attempts":
                    exit()
