"""
You have collection of thread queues which you have to poll for incoming items
much in the same way of polling multiple network connections for incoming data


Solution:
A common solution to polling problems involve a little known trick involving hidden
loopback network connection

1: Essentially for each queue that you wish to poll create a pair of connected sockets
2: You then write on one of the sockets to signal the presence of data
3: The other socket is then passed to Select system call or similar function to poll
   for the arrival of data

Note:
  def fileno(): method is what makes queue pollable using a function such as select.
  Essentially it just exposes the underlying socket descriptor used by get() function
"""

from queue import Queue
import socket
import select
import threading


class PollableQueue(Queue):
    def __init__(self):
        super().__init__()
        self.put_sock, self.get_sock = socket.socketpair()

    def fileno(self):
        return self.get_sock.fileno()

    def put(self, item):
        super().put(item)
        self.put_sock.send(b'x')

    def get(self):
        self.get_sock.recv(1)
        return super().get()


def consumer(queues):
    '''
    Consumer reads the data from multiple queues simultaneously
    :param queues:
    :return:
    '''

    while True:
        can_r, _, _ = select.select(queues, [], [])

        for queue in can_r:
            item = queue.get()
            print("Got: ", item)


q1 = PollableQueue()
q2 = PollableQueue()
q3 = PollableQueue()


def main():
    t = threading.Thread(target=consumer, args=([q1, q2, q3],))
    t.daemon = True
    t.start()


if __name__ == '__main__':
    main()
