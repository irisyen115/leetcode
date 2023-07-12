class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = 0      
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 0:
                    continue        
                ans = 0        
                q = deque([(a, b)])
                while q:
                    a1, b1 = q.popleft()
                    if  (a1 < 0 or a1 >= len(grid)) or (b1 < 0 or b1 >= len(grid[0])):
                        continue
                    if grid[a1][b1] == 0:
                        continue
                            
                    q.extend ( [(a1, b1 +1), (a1, b1 - 1), (a1 + 1, b1), (a1 - 1, b1)] )
                    grid[a1][b1] = 0   
                    ans += 1
                M = max(M, ans)
        return M
                    