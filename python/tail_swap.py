'''
https://www.codewars.com/kata/5868812b15f0057e05000001/python

DESCRIPTION:

You'll be given a list of two strings, and each will contain exactly one colon (":") in 
the middle (but not at beginning or end). The length of the strings, before and after 
the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), 
but with the characters after each colon swapped.

Examples
["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
'''

def tail_swap(strings):
    
    res = []
    
    for i in strings:
        res.append(i.split(":"))
        
    res[0][1], res[1][1] = res[1][1], res[0][1]
        
    return [":".join(x) for x in res]

# One of those katas with many different and interesting solutions!