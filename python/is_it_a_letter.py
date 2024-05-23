'''
DESCRIPTION:

Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a
letter or not.
'''

def is_it_letter(s):

    return s.isalpha()

# Lots of silly ways to do this, here's another, lol.
def is_it_letter(s):
    
    return (65 <= ord(s) <= 90) or (97 <= ord(s) <= 122)