data = ('ACME', 50, 100.5)


def main():
    print(*data)
    print(*data, sep=', ', end=" !!\n\n")
    new_data = ", ".join(*data)  # Join works only on strings but print works with all types data


if __name__ == '__main__':
    main()
