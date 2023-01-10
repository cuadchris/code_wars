# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

# DESCRIPTION:
# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.

def high(x):
    
    result = []
    sum = 0
    words = x.split()
    
    for index, word in enumerate(words):
        for letter in word:
            sum += ord(letter)-96
        result.append((index, sum))
        sum = 0
        
    return words[sorted(result, key = lambda x: x[1], reverse=True)[0][0]]

# I remember trying this one as a newbie, before I knew about the ord method. Failed miserably, lol.