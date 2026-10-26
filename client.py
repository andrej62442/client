import socket
import threading

class client_socket:
    def __init__(self,socket, username):
        self.socket = socket
        self.username = username
    def send(self,data, flags):
        self.socket.send(f"{self.username}: {data}".encode(), flags)
    def recv(self, buffSize, flags):
        return self.socket.recv(buffSize, flags).decode()
    def close(self):
        self.socket.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.8.114', 8080)
sock.connect(server_address)
c_sock = client_socket(sock, input("Type in your username: "))
print(c_sock.username)


def sending_thread(clientSocket):
    print("Hey it's me it's verity")
    print("Also try typing something\n")
    try:
        while True:
            clientSocket.send(input(), 0)
    finally:
        clientSocket.close()
        exit(-1)
def create_client_thread(c_socket):
    return threading.Thread(target=sending_thread, args=(c_socket,))


ct = create_client_thread(c_sock)
ct.start()
print("conntected wow")
try:
    while (True):
        data = c_sock.recv(1024, 0)
        print(data)
finally:
    sock.close()