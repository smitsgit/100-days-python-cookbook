from multiprocessing.connection import Client
from multiprocessing.reduction import recv_handle
import os
import socket


def worker(address):
    server = Client(address, authkey=b"peekaboo")
    server.send(os.getpid())

    while True:
        client_fileno = recv_handle(server)
        print(f"Worker Got FD {client_fileno}")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=client_fileno) as client:
            for msg in iter(lambda: client.recv(1024), b''):
                print(f"Worker received: {msg}")
                client.send(msg)


def main():
    import sys
    # if len(sys.argv) != 2:
    #     print('Usage: worker.py server_address', file=sys.stderr)
    #     raise SystemExit(1)
    worker(sys.argv[1])


if __name__ == '__main__':
    main()
