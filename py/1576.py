import string

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '?':
            return 'a'
        s = list(s)
        i = 0        
        while i < len(s):
            if s[i] == '?':                
                for v in string.ascii_lowercase:
                    if i == 0 and s[i+1] != v:
                        s[i] = v
                        break
                    elif i == len(s) -1 and s[i-1] != v:
                        s[i] = v
                        break
                    elif (i != 0 and i != len(s) -1) and s[i+1] != v and s[i-1] != v:
                        s[i] = v
                        break
            i += 1
        return ''.join(s)