'''
https://www.codewars.com/kata/598ee7b6ec6cb90dd6000061

Description:

Write a function that returns the count of characters that have to be removed in order to get a string
with no consecutive repeats.

Note: This includes any characters

Examples:

'abbbbc'  => 'abc'    #  answer: 3
'abbcca'  => 'abca'   #  answer: 2
'ab cca'  => 'ab ca'  #  answer: 1
'''

def count_repeats(txt):
    
    return sum(1 for a, b in zip(txt, txt[1:]) if a == b)