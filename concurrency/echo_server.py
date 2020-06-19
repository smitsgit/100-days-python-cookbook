"""
You can connect to this server using the programs like netcat [ nc ]

So since our server is running at localhost:15000
You can connect from terminal like => nc localhost 15000
"""

from concurrent.futures import ThreadPoolExecutor
from socket import *


def echo_client(client_sock, client_addr):
    '''
    Handle connection from the client
    '''
    print(f"Got conection from ", client_addr)
    with client_sock:
        for msg in iter(lambda: client_sock.recv(65536), b''):
            client_sock.sendall(msg)
    print("Client closed connection")


def echo_server(address):
    pool: ThreadPoolExecutor = ThreadPoolExecutor(10)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


def main():
    echo_server(('', 15000))


if __name__ == '__main__':
    main()
