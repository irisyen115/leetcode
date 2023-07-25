class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = list(sorted(set(nums)))
        i = 0
        for v in ns:
            nums[i] = v
            i += 1
        return len(ns)