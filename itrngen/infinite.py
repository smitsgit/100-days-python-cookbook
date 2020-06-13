"""
Replacing infinite while loops with iterator
"""

CHUNKSIZE = 8192


def process(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process(data)


def reader_n(s):
    '''
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.

    We are using 2nd form here.
    The only requirement is Callable must be 0 argument.
    The use of lambda is to create this 0 argument callable still supplying the
    required chunk size argument to recv
    :param s:
    :return:
    '''
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process(chunk)
