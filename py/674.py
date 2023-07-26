class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 1
        l = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                l += 1
            else:
                l = 1
            ans = max(ans, l)
        return ans