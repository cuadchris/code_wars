# https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109
 

# Follow up: Could you solve the problem in linear time and in O(1) space?

# Solution 1 (Using a Dictionary):
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        target = len(nums)/3

        seen = {}
        res = set()

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

            if seen[num] > target:
                res.add(num)

        return res
    
# Solution 2 (Boyer-Moore Majority Vote Algorithm):
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        target = len(nums) // 3
        
        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [x for x in (candidate1, candidate2) if nums.count(x) > target]