import math

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        attempt = int(str(x)[::-1].rstrip('-'))
        returnable = int(math.copysign(attempt,x))

        if attempt >= (1 << 31) - 1:
            return 0
        return returnable
        
"""
Runtime: 20 ms, faster than 64.31% of Python online submissions for Reverse Integer.
Memory Usage: 13.5 MB, less than 11.86% of Python online submissions for Reverse Integer.
"""
