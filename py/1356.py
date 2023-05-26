class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        at = []
        for v in arr:
            at.append((bin(v)[2:].count('1'), v))
        return [b for a,b in sorted(at)]