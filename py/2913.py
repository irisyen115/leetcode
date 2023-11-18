class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                a.append(set(nums[i:j+1]))
        return sum(len(s) * len(s) for s in a)