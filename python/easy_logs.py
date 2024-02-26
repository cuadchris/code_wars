'''

DESCRIPTION:

Given a logarithm base X and two values A and B, return a sum of logratihms with the base X:
logxA + logxB.


'''

from math import log

def logs(x, a, b):
    
    return log(a * b, x)