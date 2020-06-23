'''
Please watch : https://www.youtube.com/watch?v=HTLu2DFOdTg [ 34:43 ]
'''

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(self)
        perimeter = self.__perimeter()
        radius = perimeter / (2 * math.pi)
        return math.pi * radius ** 2

    def __perimeter(self):
        print("Circle's Perimeter")
        return 2 * math.pi * self.radius


class Tyre(Circle):
    def __perimeter(self):
        return Circle.perimeter(self) * 1.25


def main():
    circle = Circle(10)
    tyre = Tyre(10)

    print("Calling  circles area 314.1592653589793")
    print("Calling  tyres area 314.1592653589793")

    print(f"Calling  circles area {circle.area()}")
    print(f"Calling  tyres area {tyre.area()}")


if __name__ == '__main__':
    main()
