'''
You need to perform same operations on many objects but those
objects are contained in different containers, and you would like to
avoid nested loops without loosing the readability of the code
'''

import itertools


def main():
    first = [10, 20, 30]
    second = ["smital", "shravs", "faddu"]

    for item in itertools.chain(first, second):
        print(item)


if __name__ == '__main__':
    main()
