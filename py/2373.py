class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        maxLocal = [[0] * (len(grid) - 2)  for _ in range(len(grid) - 2)]
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                localMax = -1
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        localMax = max(localMax, grid[k][l])
                maxLocal[i-1][j-1] = localMax
        return maxLocal