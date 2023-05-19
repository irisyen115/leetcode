class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        return max(sum(value for key,value in c.items() if key > 0), sum(value for key,value in c.items() if key < 0))