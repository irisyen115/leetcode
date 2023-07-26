class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        a = []
        while i < len(nums) - 1:
            a.append((nums[i] + nums[i+1]) % 10)
            i += 1
            if i == len(nums) - 1:
                nums = a
                a = []
                i = 0
        return nums[0]