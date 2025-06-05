'''
https://www.codewars.com/kata/517abf86da9663f1d2000003

DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the
output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

Examples:

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
'''

import re

def to_camel_case(text):

    if not text:
        return ''

    # Supposedly you should never mutate the original value passed in?
    original_input = text

    pattern = "[_-][a-zA-Z]"

    match_exists = re.search(pattern, original_input)

    while match_exists:
        new_string = re.sub(pattern, match_exists.group()[1].upper(), original_input, 1)
        original_input = new_string
        match_exists = re.search(pattern, new_string)

    return original_input

# Deff overkill; but had a hard time wrapping my head around this problem.
