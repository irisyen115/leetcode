class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = Counter(nums)
        return all(value % 2 == 0 for key,value in c.items())