# https://www.codewars.com/kata/542f3d5fd002f86efc00081a/python

# DESCRIPTION:

# Prime Factors

# Inspired by one of Uncle Bob's TDD Kata

# Write a function that generates factors for a given number.

# The function takes an integer as parameter and returns a list of integers 
# (ObjC: array of NSNumbers representing integers). That list contains the prime factors in numerical 
# sequence.

# Examples
# 1  ==>  []
# 3  ==>  [3]
# 8  ==>  [2, 2, 2]
# 9  ==>  [3, 3]
# 12 ==>  [2, 2, 3]

import math
def prime_factors (n):
    
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, math.isqrt(n) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors