class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c = Counter(nums)
        k = 0
        a = []
        for key, value in c.items():
            a.extend([key] * value)
            k = max(k, value)
        return [a[i::k] for i in range(k)]