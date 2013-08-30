#!/usr/bin/python2.7
'''A simple interactive calculator'''

import sys


def add(num1, num2):
    '''Add two numbers'''
    res = num1 + num2
    return res


def sub(num1, num2):
    '''Subtract one number from another'''
    res = num1 - num2
    return res


def mult(num1, num2):
    '''Multiply two numbers'''
    res = num1 * num2
    return res


def div(num1, num2):
    '''Divide one number by another'''
    res = num1 / num2
    return res


def calculate(calc_buffer):
    '''Do the math'''
    num1 = float(calc_buffer[0])
    num2 = float(calc_buffer[2])
    oper = calc_buffer[1]
    if oper == '+':
        res = add(num1, num2)
    elif oper == '-':
        res = sub(num1, num2)
    elif oper == '*':
        res = mult(num1, num2)
    elif oper == '/':
        res = div(num1, num2)
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
