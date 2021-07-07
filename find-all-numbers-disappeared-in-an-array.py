class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(xrange(1,len(nums)+1)) - set(nums))
      
"""
Runtime: 268 ms, faster than 100.00% of Python online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 24.4 MB, less than 24.06% of Python online submissions for Find All Numbers Disappeared in an Array.
        
