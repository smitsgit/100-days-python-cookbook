from datetime import datetime


class Hello:
    def __str__(self):
        pass

    def __repr__(self):
        return "Hello()"


class Gello:
    pass


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x!s}, {self.y!s})"

    def __repr__(self):
        # return f"Pair({self.x!r}, {self.y!r})"
        return f"Pair({self.x}, {self.y})"


def main():
    lst = [Hello(), Hello(), Hello(), Gello(), Gello()]
    print(lst)
    p = Pair(datetime.now(), datetime.now())
    print(p)
    print(repr(p))


if __name__ == '__main__':
    main()
