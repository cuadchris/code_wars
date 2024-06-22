'''
https://www.codewars.com/kata/61c49a1045dba2004e7acd1f

DESCRIPTION:

Quine is a nonempty program that prints itself. Your task is bit different than that. Write a function
that takes no parameters and returns your program as a string instead of printing it.
'''

def quine():
    source_code = 'def quine():\n    source_code = {!r}\n    return source_code.format(source_code)'
    return source_code.format(source_code)

# Lots of other interesting solutions for this.
