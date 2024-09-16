'''
https://www.codewars.com/kata/563b1f55a5f2079dc100008a

DESCRIPTION:

In this kata the aim is to compare each pair of integers from two arrays, and return a new array of large
numbers.

Note: Both arrays have the same dimensions.

Example:
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
'''

get_larger_numbers = lambda a, b: [max(x, y) for x, y in zip(a, b)]

# lambdas are cool, as is the zip function.