'''
You have multiple Python interpreter processs running and you wish to pass an open
file descriptor from one interpreter to other.

For instance there is server process that is responsible for accepting connections
but the actual servicing of the client is to be handled by different interpreter

main
     -> Creates a pipe. Pipe is bi-directional [ c1, c2 ] [ Server closes the in and worker closes the out ]
     -> spawns worker first and then passes the worker_pid to server
     -> Spawns the server and server starts accepting connections

Worker -> Waits for the fileno to be sent from server
       -> Once received, it creates a socket out of it and then starts sending / receiving

Server -> After accepting connection from client, server does send_handle(out, conn.fileno(), worker_pid)
       -> Server closes the client socket cause its been already handled by worker

client -> Connects to server and eventually gets handled by worker

'''

import multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
import socket


def worker(in_p, out_p):
    out_p.close()
    while True:
        client_fileno = recv_handle(in_p)
        print(f"Worker got FD: {client_fileno}")
        # if you already have filenp of the opened socket, we can wrap a socket around it.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=client_fileno) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print(f"Worker received {msg}")
                client.send(msg)


def server(address, in_p, out_p, worker_pid):
    in_p.close()
    # This is how socket.socket() is generally used to return new socket fd
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(address)
    s.listen(1)
    while True:
        client, address = s.accept()
        print(f"Server got connection from {address}")
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()


def main():
    c1, c2 = multiprocessing.Pipe()

    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(target=server, args=(('', 15000), c1, c2, worker_p.pid))
    server_p.start()

    c1.close()
    c2.close()


if __name__ == '__main__':
    main()
