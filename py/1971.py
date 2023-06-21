class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        d = {i:i for i in range(n)}
        
        def findRoot(x):
            if x != d[x]:
                d[x] = findRoot(d[x])
            return d[x]

        for edge in edges:
            ra, rb = findRoot(edge[0]), findRoot(edge[1])            
            d[rb] = ra
            
        return d[findRoot(source)] == d[findRoot(destination)]