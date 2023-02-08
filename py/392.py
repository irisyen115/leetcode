class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        i = 0   
        for v in t:
            if i >= len(s):
                break
            if s[i] == v:                
                i += 1
        return i == len(s)