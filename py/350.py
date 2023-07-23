class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        ans = []
        for key, value in (c1 & c2).items():
            ans.extend([key] * value)
        return ans