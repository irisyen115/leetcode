class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        p = permutations(nums)  
  
        return [i for i in list(p)]
            