class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        while i < len(s) - 1:
            if i >= 0 and abs(ord(s[i]) - ord(s[i+1])) == 32:
                s.pop(i)
                s.pop(i)
                i -= 1
            else:
                i += 1
        return ''.join(s)