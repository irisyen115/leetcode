class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        def csd(s):
            a = {}
            b = ''
            c = 0
            for v in s:
                if v not in a:
                    a[v] = chr(c + 97)
                    c += 1        
                b += a[v]
            return b
        return csd(pattern) == csd(s.split())