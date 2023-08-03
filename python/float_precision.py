# https://www.codewars.com/kata/5143d157ceb46d6a61000001/python

# DESCRIPTION:

# Update the solution method to round the argument value to the closest precision of two. 
# The argument will always be a float.

# 23.23456 --> 23.23
# 1.546    --> 1.55

def solution(n):
    return int(n * 100 + 0.5) / 100.0

# Or just this
def solution(n):
    return round(n,2)