class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d = defaultdict(int) 
        for v in (nums1 + nums2):
            d[v[0]] += v[1]
        return sorted(d.items())