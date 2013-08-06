#!/usr/bin/env python2.7

import math
import argparse
import sys

class PiRound(object):
    ''' Round pi to the given digit '''
    def __init__(self, digits):
        self.digits = digits

    ''' Return the rounded pi value '''
    def get_rounded_pi(self):
        return round(math.pi, self.digits)

def main():
    ''' Parse the cmdline args ''' 
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--digits', 
        help="Number of digits to estimate pi to", required=True)
    args = parser.parse_args()

    ''' Convert input to an integer or bail '''
    try: 
        digits = int(args.digits)
    except:
        print "ERROR: must supply an integer for digits"
        sys.exit(1)

    if digits > 10:
        print "ERROR: 10 is the maximum allowed"
        sys.exit(1)

    ''' Create the PiRound object and print the rounded value '''
    pi_round = PiRound(digits)
    print "Pi to the %d digits is: %s" % (digits, pi_round.get_rounded_pi()) 

if __name__ == '__main__':
    main()
