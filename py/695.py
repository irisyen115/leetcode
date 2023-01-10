# 法1
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(x,y):            
            if  (x < 0 or x >= len(grid)) or (y < 0 or y >= len(grid[0])):
                return 0
            if grid[x][y] == 0:
                return 0
            grid[x][y] = 0                

            return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)

        M = 0        
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 0:
                    continue
                ans = dfs(a,b)
                if ans > M:
                    M = ans
        return M
# 法2
from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(x,y):
            count = 0
            q = deque()
            q.append((x,y))
            while q:
                front = q.popleft()
                if  (front[0] < 0 or front[0] >= len(grid)) or (front[1] < 0 or front[1] >= len(grid[0])):
                    continue
                if grid[front[0]][front[1]] == 0:
                    continue
                grid[front[0]][front[1]] = 0

                count += 1
                q.append((front[0]+1,front[1]))
                q.append((front[0]-1,front[1]))
                q.append((front[0],front[1]+1))
                q.append((front[0],front[1]-1))
            return count

        M = 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == 0:
                    continue
                ans = bfs(a,b)
                if M < ans:
                    M = ans
        return M    