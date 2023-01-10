# 法1
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x,y,seen):            
            if (x,y) in seen:
                return
            if  (x < 0 or x >= len(grid)) or (y < 0 or y >= len(grid[0])):
                return
            if grid[x][y] == '0':
                return
            seen.add((x,y))
            # 把鄰居也dfs一遍
            dfs(x-1, y, seen)
            dfs(x+1, y, seen)
            dfs(x, y-1, seen)
            dfs(x, y+1, seen)

        count = 0        
        p = set()
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == '0' :
                    continue
                if (a,b) in p:
                    continue                
                count += 1
                dfs(a,b,p)
        return count    

# 法2
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(x,y,seen):
            q = deque()
            q.append((x,y))
            while q:
                front = q.popleft()
                if front in seen:
                    continue
                if  (front[0] < 0 or front[0] >= len(grid)) or (front[1] < 0 or front[1] >= len(grid[0])):
                    continue
                if grid[front[0]][front[1]] == '0':
                    continue
                seen.add(front)
                q.append((front[0]+1,front[1]))
                q.append((front[0]-1,front[1]))
                q.append((front[0],front[1]+1))
                q.append((front[0],front[1]-1))

        count = 0        
        visited = set()
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == '0' :
                    continue
                if (a,b) in visited:
                    continue                
                count += 1         
                bfs(a,b,visited)       
        return count    