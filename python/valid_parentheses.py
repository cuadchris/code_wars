# https://www.codewars.com/kata/6411b91a5e71b915d237332d/python

# DESCRIPTION:
# Write a function that takes a string of parentheses, and determines if the order of the 
# parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# Constraints
# 0 <= length of input <= 100

# All inputs will be strings, consisting only of characters ( and ).
# Empty strings are considered balanced (and therefore valid), and will be tested.
# For languages with mutable strings, the inputs should not be mutated.

# Protip: If you are trying to figure out why a string of parentheses is invalid, 
# paste the parentheses into the code editor, and let the code highlighting show you!

def valid_parentheses(paren_str):
    
    res = [1 if x == "(" else -1 for x in paren_str]
    sum = 0
    
    for i in res:
        sum += i
        if sum < 0:
            return False
        
    return sum == 0