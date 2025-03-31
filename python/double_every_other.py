'''
https://www.codewars.com/kata/5809c661f15835266900010a

Description:

Write a function that doubles every second integer in a list, starting from the left.

Example:

For input array/list :

[1,2,3,4]

the function should return :

[1,4,3,8]
'''

def double_every_other(lst):
    
    return [y*2 if x%2 else y for x,y in enumerate(lst)]
