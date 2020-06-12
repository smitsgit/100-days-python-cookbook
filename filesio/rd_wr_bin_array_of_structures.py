from struct import Struct
from typing import Sequence, Tuple


def write_records(records: Sequence[Tuple], format, file):
    '''
    Write a sequence of tuples to binary file of structures
    :param records:
    :param format:
    :param file:
    :return:
    '''
    record_struct = Struct(format)

    for record in records:
        file.write(record_struct.pack(*record))


def read_records(format, file):
    record_struct = Struct(format)
    chunks = iter(lambda: file.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))
    # if you dont use unpack_from, then the offset needs to managed explicitly as shown below
    # return (record_struct.unpack(data[offset: offset + record_struct.size]) for offset in range(0, len(data), record_struct.size))


def main():
    records = [(1, 2.3, 4.5), (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open("records.bin", "wb") as file:
        write_records(records, "<idd", file)

    with open("records.bin", "rb") as file:
        for record in read_records("<idd", file):
            print(record)

    print()
    with open("records.bin", "rb") as file:
        data = file.read()
        for record in unpack_records("<idd", data):
            print(record)


if __name__ == '__main__':
    main()
