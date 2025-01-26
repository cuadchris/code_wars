'''
https://www.codewars.com/kata/585af8f645376cda59000200/python

DESCRIPTION:

You have a collection of lovely poems. Unfortunately, they aren't formatted very well. 
They're all on one line, like this:

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than 
complex. Complex is better than complicated.
What you want is to present each sentence on a new line, so that it looks like this:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Write a function, format_poem() that takes a string like the one line example as an 
argument and returns a new string that is formatted across multiple lines with each new 
     sentence starting on a new line when you print it out.

Try to solve this challenge with the str.split() and the str.join() string methods.

Every sentence will end with a period, and every new sentence will have one space before 
the previous period. Be careful about trailing whitespace in your solution.
'''

def format_poem(poem):
    return'.\n'.join(poem.split('. '))

# This one messed with me more than I thought it would. Anybody else overlook exactly
# how much you can achieve with the join function, or is it just me?

# Saw this on the solutions tab, lol!
from re import sub

# Try to solve this challenge with the str.split() and the str.join() string methods.
# -> No
def format_poem(poem):
    return sub(r"(?<=\.)\s", "\n", poem)