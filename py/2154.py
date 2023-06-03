class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        for num in sorted(nums):
            if num == original:
                original *= 2
        return original