from multiprocessing.connection import Listener
from multiprocessing.reduction import send_handle
import socket


def server(address, port):
    server = Listener(address, authkey=b"peekaboo")
    conn = server.accept()
    worker_pid = conn.recv()

    print(f"Server : Worked PID {worker_pid}")

    # This is how socket.socket() is generally used to return new socket fd
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)
    while True:
        client, address = s.accept()
        print(f"Server got connection from {address}")
        send_handle(conn, client.fileno(), worker_pid)
        client.close()


def main():
    import sys
    server(sys.argv[1], 15001)


if __name__ == '__main__':
    main()
