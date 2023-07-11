class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        t1 = m - 1
        t2 = n - 1
        tail = m + n - 1
        while t1 >= 0 and t2 >= 0:
            if nums2[t2] >= nums1[t1]:
                nums1[tail] = nums2[t2]
                t2 -= 1
            else:
                nums1[tail] = nums1[t1]
                t1 -= 1
            tail -= 1
        nums1[:t2 + 1] = nums2[:t2 + 1]
        return nums1 