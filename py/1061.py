class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        d = {}
        for v in string.ascii_lowercase:
            d[v] = v
            
        def findRoot(x):
            if x != d[x]:
                d[x] = findRoot(d[x])
            return d[x]

        for a, b in zip(s1, s2):
            ra, rb = findRoot(a), findRoot(b)
            if ra < rb:
                d[rb] = ra
            else:
                d[ra] = rb
            
        for v in baseStr:
            d[v] = findRoot(v)

        return ''.join(d[v] for v in baseStr)