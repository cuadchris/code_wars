'''
https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/python

DESCRIPTION:

Task:

Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples:
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

Notes:
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.
'''

# My basic solution.
def flick_switch(lst):
    
    flag = True
    res = []
    
    for i in lst:
        if i == 'flick':
            flag = not flag
        res.append(flag)
        
    return res

# Here's an awesome one from the site that I came across.

def flick_switch(lst):
    flick = True
    return [ (flick := flick ^ (v=='flick')) for v in lst]