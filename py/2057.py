class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = -1
        for i in range(len(nums)):
            if nums[i] == i % 10:
                a = i 
                break           
        return a