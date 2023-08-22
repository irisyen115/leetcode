class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        for i in range(len(grid)):
            if grid[i][i] == 0 or grid[i][len(grid) - 1 - i] == 0:
                return False
            for j in range(len(grid[i])):
                if (j != i and j != len(grid) - 1 - i) and grid[i][j] != 0:
                    return False
        return True