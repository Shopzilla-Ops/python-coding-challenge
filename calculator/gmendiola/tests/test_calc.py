
from nose.tools import assert_equal, assert_raises
import calc


def test__group_tokens():
    test_input = [
        1.0, '+', 2.0, '*', '(', 3.0, '-', 4.0, '/', '(', 5.0, '^', 6.0, ')',
        '+', 7.0, ')', '*', 8.0, '-', 9.0
    ]
    test_output = [
        1.0, '+', 2.0, '*',
        [
            3.0, '-', 4.0, '/',
            [
                5.0, '^', 6.0
            ],
            '+', 7.0
        ],
        '*', 8.0, '-', 9.0
    ]
    assert_equal(calc._group_tokens(test_input), test_output)


def test__parse():
    test_output = [
        1.0, '+', 2.0, '*',
        [
            3.0, '-', 4.0, '/',
            [
                5.0, '^', 6.0
            ],
            '+', 7.0
        ],
        '*', 8.0, '-', 9.0
    ]
    assert_equal(calc._parse('1+2*(3-4/(5^6)+7)*8-9'), test_output)
    test_output = [
        1.0, '+', 2.0, '*', 3.0, '-', 4.0, '/',
        5.0, '^', 6.0, '+', 7.0, '*', 8.0, '-', 9.0
    ]
    assert_equal(calc._parse('1+2*3-4/5^6+7*8-9'), test_output)


def test__reduce_expression():
    test_input = [
        1.0, '+', 2.0, '*',
        [
            3.0, '-', 4.0, '/',
            [
                5.0, '^', 6.0
            ],
            '+', 7.0
        ],
        '*', 8.0, '-', 9.0
    ]
    assert_equal(calc._reduce_expression(test_input), 151.995904)
    test_input = [1.0, 2.0, '*', 3.0]
    assert_raises(Exception, calc._reduce_expression, test_input)
    test_input = [1.0, '+', 2.0, '*']
    assert_raises(Exception, calc._reduce_expression, test_input)


def test_calculate():
    assert_equal(calc.calculate('1+2*(3-4/(5^6)+7)*8-9'), 151.995904)
    assert_raises(Exception, calc.calculate, '1+2*(3-4/(5^6)+7*8-9')
    assert_raises(Exception, calc.calculate, '1+2*)(3-4/(5^6)+7*8-9')
