import bz2
import gzip
import os
import fnmatch


def gen_find(patten, top):
    for path, _, fileslist in os.walk(top):
        for name in fnmatch.filter(fileslist, patten):
            yield os.path.join(path, name)


def gen_opener(files):
    for item in files:
        if item.endswith("*.gz"):
            file = gzip.open(item, 'rt')
        elif item.endswith("*.bz2"):
            file = bz2.open(item, 'rt')
        else:
            file = open(item, 'rt')
        yield file
        file.close()


def gen_lines(open_file_handles):
    for it in open_file_handles:
        try:
            yield from it
        except UnicodeError as e:
            print(e)


def main():
    files = gen_find('access-log*', 'www')
    open_file_handles = gen_opener(files)
    lines = gen_lines(open_file_handles)
    for line, _ in zip(lines, range(50)):
        print(line)


if __name__ == '__main__':
    main()
