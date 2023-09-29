class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        a = [i for i in range(1, m + 1)]
        
        ans = []
        for v in queries:
            ans.append(a.index(v))
            a = [a.pop(ans[-1])] + a
        return ans