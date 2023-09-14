class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(grid)
        cols = len(grid[0])
        
        row_ones = [0] * rows
        col_ones = [0] * cols
        
        for i in range(rows):
            for j in range(cols):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]
        
        ans = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                ans[i][j] = row_ones[i] + col_ones[j] - (rows - row_ones[i]) - (cols - col_ones[j])
        
        return ans