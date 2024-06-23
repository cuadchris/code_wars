'''
https://www.codewars.com/kata/56dd927e4c9055f8470013a5

DESCRIPTION:

No Story

No Description

Only by Thinking and Testing

Look at result of testcase, guess the code!

Test cases for reference:

from solution import testit
import codewars_test as test

@test.describe("Sport Star")
def sport_star():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(testit(["run","jump","run","jump","run"],"_|_|_"),"_|_|_")
        test.assert_equals(testit(["run","jump","run","run","run"],"_|_|_"),"_|_/_")
        test.assert_equals(testit(["run","run","run","run","run"],"_|_|_"),"_/_/_")
        test.assert_equals(testit(["jump","jump","jump","jump","jump"],"_|_|_"),"x|x|x")
        test.assert_equals(testit(["jump","run","jump","run","jump"],"_|_|_"),"x/x/x")
        test.assert_equals(testit(["run","run","run","run","run","run","run","run","run","run"],"||||||||||"),"//////////")
        test.assert_equals(testit(["jump","jump","jump","jump","jump","jump","jump","jump","jump","jump"],"__________"),"xxxxxxxxxx")
'''

def testit(act, s):
    
    res = []
    
    mappings = {
        "jump": "|",
        "run": "_",
        "not_run": "/",
        "not_jump": "x"
    }
    
    for action, symbol in zip(act, s):
        if mappings[action] != symbol:
            res.append(mappings[f"not_{action}"])
        else:
            res.append(symbol)
            
    return "".join(res)
