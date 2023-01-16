from collections import Counter

class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """        
        d = {}        
        ans = ''
        sort = []
        c = Counter(s)
        for i,v in enumerate(order):
            d[v] = i
        for k,v in d.items():
            sort.append((v,k))
        sort = sorted(sort)
        for a,b in sort:
            if b in s:
                ans += b * c[b]
        for k,v in c.items():
            if k not in order:
                ans += k * v
        return ans