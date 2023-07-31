class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        M = 0
        s = 0
        for i in range(len(nums) - k):
            s += float(nums[i + k] - nums[i])
            M = max(s, M)
        return (float(sum(nums[:k])) + M) / k