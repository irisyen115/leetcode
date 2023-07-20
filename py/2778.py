class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        return sum(nums[i] * nums[i] for i in range(len(nums)) if len(nums) % (i + 1) == 0)
