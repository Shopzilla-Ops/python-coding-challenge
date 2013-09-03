#!/usr/bin/python2.7
'''A series of tests to evaluate proper arithmetic and results for
the calculator.py script
'''

import unittest
import calculator


class MathTest(unittest.TestCase):
    '''The test class, contains functions for addition, subtraction,
    multiplication, and division
    '''
    testValues = [(6, 3)]

    def testAddition(self):
        '''Calculator should return the sum of two numbers'''
        for num1, num2 in self.testValues:
            result = calculator.add(num1, num2)
            self.assertEqual(9, result)

    def testSubtraction(self):
        ''''Calculator should return the difference of two numbers'''
        for num1, num2 in self.testValues:
            result = calculator.sub(num1, num2)
            self.assertEqual(3, result)

    def testMultiplication(self):
        ''''Calculator should return the product of two numbers'''
        for num1, num2 in self.testValues:
            result = calculator.mult(num1, num2)
            self.assertEqual(18, result)

    def testDivision(self):
        ''''Calculator should return the quotient of two numbers'''
        for num1, num2 in self.testValues:
            result = calculator.div(num1, num2)
            self.assertEqual(2, result)


class ParseTest(unittest.TestCase):
    '''Test the parsing of a three-string buffer'''
    testBuffer = []

    def setUp(self):
        self.testBuffer = ['6', '', '3']

    def testBufferAddition(self):
        '''Parse the + operator and add two numbers'''
        self.testBuffer[1] = '+'
        result = calculator.calculate(self.testBuffer)
        self.assertEqual('9.0', result)

    def testBufferSubtraction(self):
        '''Parse the - operator and subtract two numbers'''
        self.testBuffer[1] = '-'
        result = calculator.calculate(self.testBuffer)
        self.assertEqual('3.0', result)

    def testBufferMultiplication(self):
        '''Parse the * operator and multiply two numbers'''
        self.testBuffer[1] = '*'
        result = calculator.calculate(self.testBuffer)
        self.assertEqual('18.0', result)

    def testBufferDivision(self):
        '''Parse the / operator and multiply two numbers'''
        self.testBuffer[1] = '/'
        result = calculator.calculate(self.testBuffer)
        self.assertEqual('2.0', result)

    def testOperatorFailure(self):
        '''Parse an incorrect operator and fail properly'''
        self.testBuffer[1] = '#'
        with self.assertRaises(SystemExit) as exitcode:
            calculator.calculate(self.testBuffer)
        self.assertEqual(2, exitcode.exception.code)

if __name__ == '__main__':
    unittest.main()
