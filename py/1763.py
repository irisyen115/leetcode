class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        def niceSt(s):
            a = set(s)  
            for i,ch in enumerate(s):
                if ch.swapcase() not in a:
                    s_front = niceSt(s[:i])
                    s_back = niceSt(s[i + 1:])
                    return max(s_front,s_back,key=len)            
            return s
        return niceSt(s)