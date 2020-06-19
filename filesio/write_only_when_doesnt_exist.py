"""
You wish to write data to file system but only if it doesn't already exist
in the system.

This problem is easily solved by using little known "x" mode instead of "w" mode
"""
from contextlib import suppress


def main():
    with suppress(FileExistsError):
        with open("Hello_world.txt", "xt") as fd:
            fd.write("Gello")


if __name__ == '__main__':
    main()
