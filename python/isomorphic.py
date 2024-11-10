'''
https://www.codewars.com/kata/59dbab4d7997cb350000007f

DESCRIPTION:

Two strings a and b are called isomorphic if there is a one to one mapping possible for every character 
of a to every character of b. And all occurrences of every character in a map to same character in b.

Task
In this kata you will create a function that return True if two given strings are isomorphic to each 
other, and False otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.

Example
True:

CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
False:

AB CC
XXY XYY
ABAB CD
'''

def isomorph(a, b):
    
    if not len(a) == len(b):
        return False
    
    seen = {}
    seen2 = set()
    
    for x,y in enumerate(a):
        if y not in seen and b[x] not in seen2:
            seen[y] = b[x]
            seen2.add(b[x])
        elif y not in seen and b[x] in seen2 or y in seen and seen[y] != b[x]:
            return False
        
    return True

# favorited this one so I can come back to it.
