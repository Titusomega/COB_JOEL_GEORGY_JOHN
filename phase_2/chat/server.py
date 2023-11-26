import socket
import sys
import time
def server_side():
    new_socket_conn = socket.socket()
    host_name = socket.gethostname()
    socket_ip = socket.gethostbyname(host_name)
    port_num = 8080

    new_socket.bind((host_name, port_num))
    print("Binding successful!")
    print("This is your IP: ", socket_ip)

    name = input('Enter name:')
    new_socket.listen(1)

    conn, add = new_socket.accept()
    print("Received connection from ", add[0])
    print('Connection Established. Connected From: ', add[0])

    client_name = (conn.recv(1024)).decode()
    print(client_name + ' has connected.')
    conn.send(name.encode())

    while True:
        msg = input('Me : ')
        conn.send(msg.encode())
        msg = conn.recv(1024)
        msg = message.decode()
        print(client_name, ':', msg)  