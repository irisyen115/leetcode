class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c = Counter(s)
        d = Counter(t)
        return (d-c).keys()[0]
        