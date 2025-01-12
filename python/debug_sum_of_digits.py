'''
https://www.codewars.com/kata/563d59dd8e47a5ed220000ba

DESCRIPTION:

Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits. 
Assume that argument is an integer.

Example:

123  => 6
223  => 7
1337 => 14
'''

def get_sum_of_digits(num):
    return sum(int(x) for x in str(num))
