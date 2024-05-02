'''
In logic, an implication (or material conditional) states that If p is true, q should be true too.

We can express the result of any implication of two statements as a logical table:

p\q T F      
T   T F
F   T T

In this kata, we will take that further. Given an array (return false if the array is empty), assume that
from first to last item in the array, each implies the next (for example, in an array of three items, p, q, and r:
(p->q)->r. Return the boolean answer.

Assume that there will be no more than 8 variables in the array, and the array will contain only boolean values.
'''

def mult_implication(lst):

    res = None

    for boolean in lst:
        if res == boolean:
            res = True
        else:
            res = boolean
            
    return res