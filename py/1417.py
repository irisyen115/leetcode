class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = sum(v.isalpha() for v in s)
        d = sum(v.isdigit() for v in s)
        if abs(a - d) > 1: return ""        
        ans = [''] * len(s)        
        if a >= d:
            i = 0 
            j = 1
        else:
            i = 1 
            j = 0
        for v in s:            
            if v.isalpha():
               ans[i] = v
               i += 2
            else:
                ans[j] = v
                j += 2
        return ''.join(ans)