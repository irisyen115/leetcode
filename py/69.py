class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x+1
        while left + 1 < right:
            middle = (left+right)//2
            if middle * middle <= x: 
                left = middle
            else: 
                right = middle
        return left
        
