'''
https://www.codewars.com/kata/559e10e2e162b69f750000b4/python

DESCRIPTION:

A zero-indexed array arr consisting of n integers is given. The dominator of array arr 
is the value that occurs in more than half of the elements of arr.

For example, consider array arr such that arr = [3,4,3,2,3,1,3,3]

The dominator of arr is 3 because it occurs in 5 out of 8 elements of arr and 5 is more 
than a half of 8.

Write a function dominator(arr) that, given a zero-indexed array arr consisting of n 
integers, returns the dominator of arr. The function should return −1 if array does not 
have a dominator.

All values in arr will be >=0.
'''

def dominator(arr):
    
    seen = {}
    half = len(arr)/2
    
    for num in arr:
        seen[num] = seen.get(num, 0) + 1
        if seen[num] > half:
            return num
        
    return -1