"""
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true


Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true


Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

# This was my initial brute force solution that literally builds an array of indices for each dictionary key
# and loops through each one until 'nums[i] == nums[j] and abs(i - j) <= k' is satisfied. If it can't find it,
# it'll return False.
# Time complexity of O(n^2) due to the nested loop running through 'seen'.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = [idx]
            else:
                seen[num].append(idx)

        for i in seen:
            if len(seen[i]) > 1:
                for x,y in enumerate(seen[i]):
                    for a in seen[i][x+1:]:
                        if abs(y - a) <= k:
                            return True
                        
        return False
    
# The Sliding window strategy brings this problem back down to O(n) time complexity.
# Significantly more efficient, although not as interesting, lol.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        slider = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                slider.remove(nums[left])
                left += 1
            if nums[right] in slider:
                return True
            slider.add(nums[right])

        return False