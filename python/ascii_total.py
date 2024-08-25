'''
https://www.codewars.com/kata/572b6b2772a38bc1e700007a

Description:

You'll be given a string, and have to return the sum of all characters as an int. The function should be
able to handle all printable ASCII characters.

Examples:

uniTotal("a") == 97
uniTotal("aaa") == 291
'''

def uni_total(s):
    
    return sum(ord(x) for x in s)
