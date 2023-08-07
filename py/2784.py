class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        M = max(nums)
        s = {v + 1 for v in range(M)}
        return len(nums) == M + 1 and all(v and nums.count(v) == 1 in s for v in nums if v != M) and nums.count(M) == 2