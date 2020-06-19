'''
You wish to create a pool of workers threads for serving clients or performing other kinds
of work
'''
from concurrent.futures import ThreadPoolExecutor
import time
import threading

pool: ThreadPoolExecutor = ThreadPoolExecutor(5, thread_name_prefix='smits')


def work(sleep):
    print(f"{threading.current_thread().name}: sleeping for {sleep}s")
    time.sleep(sleep)
    print(f"{threading.current_thread().name}: Woken after {sleep}s")


def main():
    fut = []
    for item in range(1, 10):
        fut.append(pool.submit(work, item))

    for item in fut:
        item.result()


if __name__ == '__main__':
    main()
