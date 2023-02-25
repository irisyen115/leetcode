class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i,v in enumerate(s):
            if v not in d:
                d[v] = i
        M = -1
        for i in range(len(s)):
            M = max((i - d[s[i]] - 1), M)
        return M