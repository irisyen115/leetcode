class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ds = {}
        dt = {}
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = []
            if t[i] not in dt:
                dt[t[i]] = []                
            if ds[s[i]] != dt[t[i]]:
                return False
            else:
                ds[s[i]].append(i)            
                dt[t[i]].append(i)
        return True