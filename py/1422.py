class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = -1
        for i in range(len(s)-1):
            l = s[:i+1]
            r = s[i+1:]
            if l.count('0') + r.count('1') > m:
                m = l.count('0') + r.count('1')
        return m