class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(nums):
            for i2, y in enumerate(nums[i+1:], start=i+1):
                if x + y == target:
                    return i,i2
                  
"""
Runtime: 3040 ms, faster than 29.14% of Python online submissions for Two Sum.
Memory Usage: 14.1 MB, less than 78.91% of Python online submissions for Two Sum.
"""
