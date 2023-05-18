class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        count = 0
        while grid[0]:
            s = set()
            for arr in grid:            
                s.add(max(arr))
                arr.remove(max(arr))
            count += max(s)
        return count