class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        c = Counter(nums)
        for key,value in c.items():
            if value > len(nums) / 2:
                return key