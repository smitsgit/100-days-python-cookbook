"""
You want your object to support custom formating through format method
"""

_formats = {
    'ymd': "{d.year} {d.month} {d.day}",
    'myd': "{d.month} {d.year} {d.day}",
    'dmy': "{d.day} {d.month} {d.year}",
}


class MyDate:
    def __init__(self, year, month, day):
        self.day = day
        self.month = month
        self.year = year

    def __format__(self, code):
        if code == '':
           code = 'ymd'

        fmt = _formats[code]
        return fmt.format(d=self)


if __name__ == '__main__':
    date = MyDate(2016, 10, 5)
    print(format(date, 'myd'))
