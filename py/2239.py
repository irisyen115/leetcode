class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 1000000
        d = {v:abs(v) for v in nums}
        m = min([value for key, value in d.items()])
        ans = max([key for key, value in d.items() if d[key] == m])
        return ans