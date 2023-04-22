class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [0] * len(nums)
        right = [0] * len(nums)
        for i in range(1, len(nums)):
            left[i] = nums[i-1] +left[i-1]
        for i in range(1, len(nums)):
            right[-i-1] = nums[-i] + right[-i]
        return [abs(left[i]-right[i]) for i in range(len(left))]