class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = [0] * (len(nums) - 1)
        for i in range(len(nums)):
            if seen[nums[i] - 1] != 0:
                return nums[i]
            seen[nums[i] - 1] = nums[i]