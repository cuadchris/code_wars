# https://leetcode.com/problems/valid-anagram/description/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or
# phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False
        
        tallyS, tallyT = {}, {}

        for i in range(len(s)):
            tallyS[s[i]] = 1 + tallyS.get(s[i], 0)
            tallyT[t[i]] = 1 + tallyT.get(t[i], 0)

        return tallyS == tallyT

# I think you can sort both strings and compare them, but that wouldn't be very efficient?