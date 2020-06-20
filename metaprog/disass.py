'''
You want to know what your code is doing under the covers
by disassembling it into lower level byetcode used by interpreter
'''

import dis


def countdown(n):
    while n > 0:
        print('T-minus ', n)
        n -= 1
    print('Blast off !!')


def main():
    print(dis.dis(countdown))


if __name__ == '__main__':
    main()

# '''
# One observation is every instruction takes 2 bytes
# Even the ones without the argument
# For example take a look at
#              24 INPLACE_SUBTRACT
#              26 STORE_FAST               0 (n)


#  10           0 SETUP_LOOP              30 (to 32)
#         >>    2 LOAD_FAST                0 (n)
#               4 LOAD_CONST               1 (0)
#               6 COMPARE_OP               4 (>)
#               8 POP_JUMP_IF_FALSE       30
#
#  11          10 LOAD_GLOBAL              0 (print)
#              12 LOAD_CONST               2 ('T-minus ')
#              14 LOAD_FAST                0 (n)
#              16 CALL_FUNCTION            2
#              18 POP_TOP
#
#  12          20 LOAD_FAST                0 (n)
#              22 LOAD_CONST               3 (1)
#              24 INPLACE_SUBTRACT
#              26 STORE_FAST               0 (n)
#              28 JUMP_ABSOLUTE            2
#         >>   30 POP_BLOCK
#
#  13     >>   32 LOAD_GLOBAL              0 (print)
#              34 LOAD_CONST               4 ('Blast off !!')
#              36 CALL_FUNCTION            1
#              38 POP_TOP
#              40 LOAD_CONST               0 (None)
#              42 RETURN_VALUE
# None
# '''
