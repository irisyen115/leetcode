class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(heights[i] != sorted(heights)[i] for i in range(len(heights)))