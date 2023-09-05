class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count += (nums[i] + nums[j] < target)
        return count