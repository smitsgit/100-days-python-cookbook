'''
Iterating in sorted order over merged sorted iterables

The iterative nature of heapq.merge means that, it never reads supplied sequences
all at once.
This means that you can use it on long sequences with very little overhead.


'''

import heapq


def main():
    first = [1, 4, 8, 10]
    second = [2, 5, 9, 11]

    for item in heapq.merge(first, second):
        print(item)

    with open("sorted_file_1.txt") as file1, \
            open("sorted_file_2.txt") as file2, \
            open("merged_file.txt") as out:
        for line in heapq.merge(file1, file2):
            out.write(line)


# Its important to realize that heapq.merge() requires that all of the input
# sequences be sorted. In particular it doesn't read all the sequences in heap
# or do any preliminary sorting

# Nor does it perform any kind of validation of the inputs to check if they meet
# the ordering requirements.

# It simply examines the set of items from front the front of each input sequence and emit
# the smallest one found

# A new item from the chosen sequences is read again and the process is repeated until all
# the input sequences be fully consumed.

if __name__ == '__main__':
    main()
