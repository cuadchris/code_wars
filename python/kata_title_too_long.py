'''
https://www.codewars.com/kata/574b1916a3ebd6e4fa0012e7/python

DESCRIPTION:

Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result 
should be a boolean value, instead of a string.

The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that 
the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are 
empty then you should return false/False.

Examples:

(input -> output)
"ab","AB"     -> true
"aB","Ab"     -> true
"aBcd","AbCD" -> true
"AB","Ab"     -> false
"",""         -> false
'''

def is_opposite(s1,s2):
    
    if not s1 and not s2:
        return False
    
    for i in zip(s1, s2):
        if i[0].swapcase() != i[1]:
            return False
        
    return True

# That was my initial solution before I figured out that swapcase() works on the entire string. The use of zip is
# pretty cool.

# Refactored solution.
def is_opposite(s1, s2):

    return False if not(s1 or s2) else s1.swapcase() == s2
