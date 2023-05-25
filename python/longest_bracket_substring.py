# https://www.codewars.com/kata/584c3e45710dca21be000088/python

# DESCRIPTION:
# When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, 
# to enjoy the process --myjinxin2015 said

# Description:
# Given a string str consisting of some number of "(" and ")" characters, your task is to find the longest 
# substring in str such that all "(" in the substring are closed by a matching ")". The result is the 
# length of that substring.

# For example:

# "()()(" => 4
# Because "()()" is the longest substring, which has a length of 4
# Note:
# All inputs are valid.
# If no such substring found, return 0.
# Please pay attention to the performance of code. ;-)
# In the performance test(100000 brackets str x 100 testcases), the time consuming of each test case 
# should be within 35ms. This means, your code should run as fast as a rocket ;-)

# Some Examples

#  "" => 0
# "()" => 2
# "()(" => 2
# "()()" => 4
# "()()(" => 4
# "(()())" => 6
# "(()(())" => 6
# "())(()))" => 4
# "))((" => 0

def find_longest(st):
    
    max_length = 0
    stack = []
    start = -1

    for i, char in enumerate(st):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    max_length = max(max_length, i - start)
            else:
                start = i

    return max_length