class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        d = {i:i for i in range(len(isConnected))}

        def findRoot(x):
            if x != d[x]:
                d[x] = findRoot(d[x])
            return d[x]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                ri, rj = findRoot(i), findRoot(j)
                if isConnected[i][j] == 1:
                    d[rj] = ri
                    
        return len(set(d.values()))