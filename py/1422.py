class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s[0] == '0'
        r = s[1:].count('1')
        M = l + r
        for i in range(1,len(s)-1):
            if s[i] == '0':
                l += 1
            else:
                r -= 1
            M = max(M, l + r)
        return M