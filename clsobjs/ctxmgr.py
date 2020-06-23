'''
To try out this, first start two terminal sessions with
python -m http.server --bind 127.0.0.1 15000
python -m http.server --bind 127.0.0.1 17000
'''

from contextlib import contextmanager
from socket import *


@contextmanager
def LazyConn(addr, family=AF_INET, type=SOCK_STREAM):
    sock = socket(family, type)
    sock.connect(addr)

    yield sock

    sock.close()


def main():
    with LazyConn(('', 15000)) as s:
        with LazyConn(('', 17000)) as s1:
            print(s)
            print(s1)


if __name__ == '__main__':
    main()
