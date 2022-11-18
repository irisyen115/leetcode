class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        c = set(s)
        for a in c:
            if a.upper() in c and a.lower() in c:
                ans += a.upper()
        if ans:
            return max(ans)
        else:
            return ans