class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        return [len(set(nums[:i+1])) - len(set(nums[i+1:])) for i in range(len(nums))]