class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums1)
        for i in range(len(nums1)):
            h = nums2.index(nums1[i]) + 1
            if h > len(nums2) - 1:
                ans[i] = -1
                continue
            large = [j for j in range(h, len(nums2)) if nums2[j] > nums1[i]]
            if large:
                j = min(large)
            if nums1[i] < nums2[j]:
                ans[i] = nums2[j]
            else:
                ans[i] = -1
        return ans