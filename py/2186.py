from collections import Counter
import string

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        x = Counter(s)
        y = Counter(t)
        count = 0
        for v in string.ascii_lowercase:
            if x[v] < y[v]:
                count += y[v] - x[v]
            if x[v] > y[v]:
                count += x[v] - y[v]
        return count