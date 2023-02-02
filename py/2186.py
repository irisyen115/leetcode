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
        return sum(abs(x[v] - y[v]) for v in string.ascii_lowercase)