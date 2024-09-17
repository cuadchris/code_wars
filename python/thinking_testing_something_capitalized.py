'''
https://www.codewars.com/kata/56d93f249c844788bc000002/javascript

DESCRIPTION:

No Story

No Description

Only by Thinking and Testing

Look at result of testcase, guess the code!

'''

def testit(s):
    
    return ' '.join(x[:-1] + x[-1].upper() for x in s.split())