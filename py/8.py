class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ''
        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            ans += s[i]
            i += 1

        while i < n and s[i].isdigit():
            ans += s[i]
            i += 1

        if ans in ('', '+', '-'):
            return 0
        else:
            result = int(ans)
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31
            return max(min(result, INT_MAX), INT_MIN)