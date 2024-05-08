'''
https://www.codewars.com/kata/63f3c61dd27f3c07cc7978de/python

DESCRIPTION:
You are given 2 two-digit numbers. You should check if they are similar by comparing their numbers, 
and return the result in %.

Example:

compare(13,14)=50%;
compare(23,22)=50%;
compare(15,51)=100%;
compare(12,34)=0%.
'''

def compare(a, b):
    
    a = [x for x in str(a)]
    b = [x for x in str(b)]
    matches = 0
        
    for x in a:
        if x in b:
            b.remove(x)
            matches += 1

    return f'{int(matches/2*100)}%'

# overkill for sure. another busy day.
