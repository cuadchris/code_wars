'''
https://www.codewars.com/kata/59fca81a5712f9fa4700159a/python

DESCRIPTION:

Task Overview
Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in 
a binary format.

to_binary(1)   should return 1 
to_binary(5)   should return 101
to_binary(11)  should return 1011
'''

def to_binary(n, res = ''):

    if n == 0:
        return int(res)
    
    res = str(n % 2) + res
    
    return to_binary(n//2, res)

# Decided to have fun with recursion. So many other cool solutions on codewars.
