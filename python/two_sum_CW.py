'''
https://www.codewars.com/kata/52c31f8e6605bcc646000082/python

DESCRIPTION:

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) returns [0, 2] or [2, 0]
'''

def two_sum(numbers, target):
    
    seen = {}
    
    for index, num in enumerate(numbers):
        diff = target - num
        if diff in seen:
            return (index, seen[diff])
        else:
            seen[num] = index

# same problem as the one on LeetCode; never saw it on CodeWars before. Easy 6kyu, lol.