from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        c1 = Counter(s)
        c2 = Counter(t)
        m = 0
        for k,v in c2.items():
            if v - c1[k] > 0:
                m += v - c1[k]
        return m