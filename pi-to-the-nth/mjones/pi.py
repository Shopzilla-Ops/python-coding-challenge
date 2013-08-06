#!/usr/bin/python2.7

import sys

def arctan(x, fixed):
## Calculate arctan(1/x)
## This calculates it in fixed point, using the value passed in
  power = fixed // x            # the +/- 1/x**n part of the term
  total = power               # the total so far
  x_squared = x * x           # precalculate x**2
  divisor = 1                 # the 1,3,5,7 part of the divisor
  while True:
      power = - power // x_squared
      divisor += 2
      delta = power // divisor
      if delta == 0:
        break
      total += delta
  return total

def pi_machin(fixed):
## Use machin's formula for pi
  return 4*(4*arctan(5, fixed) - arctan(239, fixed))

if __name__ == "__main__":
## Should really use an argparser, but didn't have time :(
  num = int(sys.argv[1])
  unity = 10**1000

  if type(num) is not int:
    print "Parameter passed is not an integer"
    sys.exit(1)

  if num < unity:
    result = pi_machin(unity)
    print str(result)[:num+1]
    print str(result)[num]
  else:
    print "Submitted request is over the limit of 10**1000."
    sys.exit(1)
