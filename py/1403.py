class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        c = 0        
        for v in list(reversed(sorted(nums))):
            a.append(v)
            c += v
            if c > sum(nums) - c:
                break        
        return list(reversed(sorted(a)))