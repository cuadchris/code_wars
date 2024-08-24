'''
https://www.codewars.com/kata/5a90f6d457c5624ecc000012

Description:

The challenge is to efficiently find the largest pronic number less than the method's input.

The initial solution passes the sample tests, but fails for larger numbers used in the acceptance tests.

Your algorithm should be fast as the acceptance tests will run 10,000 randomly selected numbers.

Are you up to the challenge?
'''

import math

def next_smaller_pronic(n):
    
    if n <= 0:
        return 0

    k = int((math.sqrt(4 * n - 1) - 1) // 2)

    while k >= 0:
        pronic = k * (k + 1)
        if pronic < n:
            return pronic
        k -= 1

    return 0
