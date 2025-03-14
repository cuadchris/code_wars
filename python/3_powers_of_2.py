'''
https://www.codewars.com/kata/6545283611df271da7f8418c

DESCRIPTION:

Write a function three_powers() to accept a number, to check can it represent as sum of 3 powers of 2.
(n == 2**i + 2**j + 2**k, i, j, k >= 0)

For example:

three_powers(2)  # False
three_powers(3)  # True, 3 = 2**0 + 2**0 + 2**0
three_powers(5)  # True, 5 = 2**0 + 2**1 + 2**1
three_powers(15)  # False

Input:

- `n` must be an integer.
- `1` <= `n` <= `2 ** 100 - 1`

There are 2000 random tests for the speed test, good luck and happy coding.
'''

def three_powers(n):
    return n > 2 and n.bit_count() <= 3