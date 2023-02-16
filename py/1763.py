class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = set(s)  
        for i,ch in enumerate(s):
            if ch.swapcase() not in a:
                return max(self.longestNiceSubstring(s[:i]) ,self.longestNiceSubstring(s[i + 1:]),key=len)            
        return s
