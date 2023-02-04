class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        i = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        while i < len(s):
            if i < len(s) - 1 and s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                ans -= 1
            elif i < len(s) - 1 and s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C'):
                ans -= 10
            elif i < len(s) - 1 and s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M'):
                ans -= 100
            else:
                ans += d[s[i]]
            i += 1
        return ans