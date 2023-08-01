class Solution(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        trans = [col for col in zip(*grid)] 
        ans = [0] * len(trans)
        for i in range(len(trans)):
            M = 0
            for j in range(len(trans[i])):
                M = max(M, len(str(trans[i][j])))
            ans[i] = M
        return ans