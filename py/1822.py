class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        for num in nums:
            p *= num
        
        if p > 0:
            return 1
        elif p == 0:
            return 0
        else:
            return -1