'''
https://www.codewars.com/kata/5340298112fa30e786000688

DESCRIPTION:

The objective is to return all pairs of integers from a given array of integers that have a 
difference of 2.

The result array should be sorted in ascending order of values.

Assume there are no duplicate integers in the array. The order of the integers in the input 
array should not matter.

Examples:

[1, 2, 3, 4]  should return [(1, 3), (2, 4)]

[4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

[1, 23, 3, 4, 7] should return [(1, 3)]

[4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]
'''

def twos_difference(lst):
    return sorted([(x, y) for y in lst for x in lst if y - x == 2])
