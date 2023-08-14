class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = max(nums)
        for v in nums:
            if v != n and v * 2 > n:
                return -1
        return nums.index(n)