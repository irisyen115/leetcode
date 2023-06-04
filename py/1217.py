class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        o = 0
        e = 0
        for v in position:
            if v % 2 == 0:
                e += 1
            else:
                o += 1
        return min(o, e)