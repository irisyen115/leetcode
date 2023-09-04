class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return -1 if not set(nums1) & set(nums2) else min(set(nums1) & set(nums2))