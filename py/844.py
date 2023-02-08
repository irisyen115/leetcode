class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        i = 0
        while i < len(s):
            if i == 0 and s[i] == '#':
                s.remove('#')
            elif i > 0 and s[i] == '#':
                s.pop(i-1)
                s.remove('#')
                i -= 1
            else:
                i += 1
        i = 0
        while i < len(t):
            if i == 0 and t[i] == '#':
                t.remove('#')
            elif i > 0 and t[i] == '#':
                t.pop(i-1)
                t.remove('#')
                i -= 1
            else:
                i += 1
        return s == t