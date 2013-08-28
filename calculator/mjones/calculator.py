#!/usr/bin/python2.7
'''A simple interactive calculator'''

import sys


def add(int1, int2):
    '''Add two integers'''
    res = int1 + int2
    return res


def sub(int1, int2):
    '''Subtract one integer from another'''
    res = int1 - int2
    return res


def mult(int1, int2):
    '''Multiply two integers'''
    res = int1 * int2
    return res


def div(int1, int2):
    '''Divide one integer by another'''
    res = int1 / int2
    return res


def calculate(calc_buffer):
    '''Do the math'''
    int1 = int(calc_buffer[0])
    int2 = int(calc_buffer[2])
    oper = calc_buffer[1]
    if oper == '+':
        res = add(int1, int2)
    elif oper == '-':
        res = sub(int1, int2)
    elif oper == '*':
        res = mult(int1, int2)
    elif oper == '/':
        res = div(int1, int2)
    else:
        print "Invalid operator: %s" % oper
        sys.exit(2)
    return str(res)

if __name__ == "__main__":
    '''Main loop'''
    last = ''
    calc_buffer = []
    print "Let's start!"
    while True:
        try:
            input_var = str(raw_input("{%s}  " % last))
            if input_var == '=':
                break
            calc_buffer.append(input_var)
            if len(calc_buffer) == 3:
                res = calculate(calc_buffer)
                calc_buffer = [res, ]
                last = res
            else:
                last = input_var
        except KeyboardInterrupt:
            break
    print "\nFinal Result: %s\n" % last
