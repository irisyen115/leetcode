class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        return [[v for v in set(nums1) - set(nums2)], [v for v in set(nums2) - set(nums1)]]