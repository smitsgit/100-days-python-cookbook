def main():
    with open("somefile.txt", "w") as out:
        print("Hello World ###", file=out)


if __name__ == '__main__':
    main()