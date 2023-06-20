class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        e = 0
        d = {i:i for i in range(1, len(edges)+1)}
        
        def findRoot(x):
            if x != d[x]:
                d[x] = findRoot(d[x])
            return d[x]

        for edge in edges:
            ra, rb = findRoot(edge[0]), findRoot(edge[1])
            if ra == rb:
                return edge
            d[rb] = ra