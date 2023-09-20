'''
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
'''

# This was my initial solution after glancing over the problem statement.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen_set = set()

        for num in nums:
            if num in seen_set:
                return num
            seen_set.add(num)

# However, there's an additional constraint that I initially overlooked: 'You must solve the problem without
# modifying the array nums and using only constant extra space.' This significantly increases the complexity of
# the problem. I've been exploring Floyd's Cycle Detection Algorithm, also known as The Tortoise and Hare
# Algorithm. I am currently working on gaining a deeper understanding of its workings.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow