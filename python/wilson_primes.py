'''
Description:

Wilson primes satisfy the following condition. Let P represent a prime number.

Then: ((P - 1)! + 1) / (P * P)

should give a whole number, where P! is the factorial of P.

Your task is to create a function that returns true if the given number is a Wilson prime and false
otherwise.
'''

# cop out solution, but this is a bad kata.
def am_i_wilson(n):
    
    return n in (5, 13, 563)