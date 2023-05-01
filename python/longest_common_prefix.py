# https://leetcode.com/problems/longest-common-prefix/description/

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        word = strs[0]
        bools = []

        for i in range(len(word), 0, -1):
            prefix = word[:i]
            
            for i in range(1, len(strs)):
                if strs[i].startswith(prefix):
                    bools.append(True)
                else:
                    bools.append(False)

            if all(bools):
                return prefix
            else:
                bools = []

        return ''
    
# The initial ugly, and brute forcy version of solution. Will come back and optimize.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ''

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or not strs[j][i] == strs[0][i]:
                    return res

            res += strs[0][i]

        return res
    
# In this solution we're not wasting space with an extra array anymore, and we're building 
# up the prefix from the beginning, rather than looping backwards. I like both.