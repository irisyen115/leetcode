class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d = defaultdict(int)

        trans = ([col for col in zip(*grid)])
        grid = ([tuple(row) for row in grid])
        
        for row in grid:
            d[row] += 1

        count = 0
        for col in trans:    
            count += d[col]

        return count