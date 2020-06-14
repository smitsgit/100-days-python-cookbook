'''
Flattening a nested sequence.
yield from statement is a nice shortcut if you want to write generators
that call other generators or coroutines.
'''

from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from flatten(item)
            # for x in flatten(items):
            #     yield x
        else:
            yield item


def main():
    for item in flatten([1, 3, [3, 4, [5, 6, 7]]]):
        print(item)


if __name__ == '__main__':
    main()
