class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """        
        a, max_k = [], sorted(nums, reverse=True)[:k]
        for num in nums:
            if num in max_k:
                a.append(num)
                max_k.remove(num)
                if len(max_k) == 0:
                    return a
