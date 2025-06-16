'''
https://www.codewars.com/kata/54530f75699b53e558002076/python

DESCRIPTION:
Complete the function word (string) and returns a string that spells the word using the 
NATO phonetic alphabet.

There should be a space between each word in the returned string, and the first letter 
of each word should be capitalized.

For those of you that don't want your fingers to bleed, this kata already has a dictionary 
typed out for you.

Examples
"hi"      -->  "Hotel India"
"abc"     -->  "Alpha Bravo Charlie"
"babble"  -->  "Bravo Alpha Bravo Bravo Lima Echo"
"Banana"  -->  "Bravo Alpha November Alpha November Alpha"
'''
  
def nato(word):
    
    # LETTERS is preloaded
    return ' '.join(LETTERS[x] for x in word.upper())
