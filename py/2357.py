class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        while max(nums) > 0:
            nums[:] = (v for v in nums if v != 0)
            nums = [v - min(nums) for v in nums]
            count += 1
        return count