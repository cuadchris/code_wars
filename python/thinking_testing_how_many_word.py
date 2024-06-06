'''
DESCRIPTION:

No Story

No Description

Only by Thinking and Testing

Look at the results of the testcases, and guess the code!
'''

# Test cases for clues.

from solution import testit
import codewars_test as test

@test.describe("How many 'word'")
def how_many_word():
    
    @test.it("Example tests")
    def example_tests():
        test.assert_equals(testit("word"), 1)
        test.assert_equals(testit("hello world"), 1)
        test.assert_equals(testit("I love codewars."), 0)
        test.assert_equals(testit("My cat waiting for a dog."), 1)
        test.assert_equals(testit("We often read book, a word hidden in the book."), 2)
        test.assert_equals(testit("When you in order to do something by a wrong way, your heart will missed somewhere."), 2)
        test.assert_equals(testit("This sentence has one word."), 1)
        test.assert_equals(testit("This sentence has two words, not one word."), 2)
        test.assert_equals(testit("One word + one word = three words -)"), 3)
        test.assert_equals(testit("Can you find more word for me?"), 1)

# My solution.
import re

def testit(s):
    
    return len(re.findall(r'(w).*?(o).*?(r).*?(d)', s, re.IGNORECASE))