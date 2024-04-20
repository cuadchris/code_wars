'''
https://www.codewars.com/kata/58552bdb68b034a1a80001fb

DESCRIPTION:

You need to cook pancakes, but you are very hungry. As known, one needs to fry a pancake one minute on
each side. What is the minimum time you need to cook n pancakes, if you can put on the frying pan only m
pancakes at a time? n and m are positive integers between 1 and 1000.
'''

from math import ceil

def cook_pancakes(n, m):
    
    sides = n * 2
    
    mins = ceil(sides/m)
    
    return mins if mins > 1 else 2

# This one was annoying.
