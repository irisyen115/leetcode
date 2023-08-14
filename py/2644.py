class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        d = {}
        for v in divisors:
            if v not in d:
                d[v] = sum(num % v == 0 for num in nums)

        ans = min(divisors)

        for key, value in d.items():
            if value > d[ans] or (value == d[ans] and key < ans):
                ans = key
        return ans