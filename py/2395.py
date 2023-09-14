class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in range(1, len(nums)):
            if nums[i - 1] + nums[i] in s:
                return True
            s.add(nums[i - 1] + nums[i])
        return False