# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        
        result, x_remaining = 0, abs(x)

        while x_remaining:
            # Check for overflow before updating the result
            if result > (INT_MAX - x_remaining % 10) // 10:
                return 0
            result = result * 10 + x_remaining % 10
            x_remaining //= 10

        return -result if x < 0 else result