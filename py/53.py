class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('-inf')
        count = 0
        for num in nums:
            count = count + num
            if count > ans:
                ans = count
            if count < 0:
                count = 0
        return ans