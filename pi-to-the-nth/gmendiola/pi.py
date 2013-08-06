#!/usr/bin/python2.7

'''
This module provides a unbounded stream generator for the digits a pi.
It utilizes the algorithm by Jeremy Gibbons outlined here:

http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf


Here's the original algorithm:

pi = g(1,0,1,1,3,3) where
g(q,r,t,k,n,l) = if 4*q+r-t<n*t
then n : g(10*q,10*(r-n*t),t,k,div(10*(3*q+r))t-10*n,l)
else g(q*k,(2*q+r)*l,t*l,k+1,div(q*(7*k+2)+r*l)(t*l),l+2)
'''

import sys
import argparse


def iter_pi():
    '''This generator yields a stream of digits from pi'''
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if ((4 * q) + r - t) < (n * t):
            yield n
            (q, r, t, k, n, l) = (
                10 * q,
                10 * (r - (n * t)),
                t,
                k,
                ((10 * ((3 * q) + r)) // t) - (10 * n),
                l
            )
        else:
            (q, r, t, k, n, l) = (
                q * k,
                ((2 * q) + r) * l,
                t * l,
                k + 1,
                (q * ((7 * k) + 2) + r * l) // (t * l),
                l + 2
            )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print pi to n digits.')
    parser.add_argument('digits', type=int, help='Number of digits to print')
    args = parser.parse_args()
    pi_digits = iter_pi()
    sys.stdout.write(str(pi_digits.next()) + '.')
    for d in range(args.digits):
        sys.stdout.write(str(pi_digits.next()))
    print ''
