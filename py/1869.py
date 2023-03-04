class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """      
        d = {'0': 0, '1': 0}
        for x, y in itertools.groupby(s):
            d[x] = max(d[x], sum(1 for _ in y))
        return d['1'] > d['0']