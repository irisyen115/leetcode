class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 1
        a = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                a += 1
            else:
                a = 1
            M = max(M,a)
        return M