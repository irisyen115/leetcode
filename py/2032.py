class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        return [v for v in list(set(nums1 + nums2 + nums3)) if (v in nums1 and v in nums2) or (v in nums2 and v in nums3) or (v in nums1 and v in nums3)]