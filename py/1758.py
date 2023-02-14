class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        counta = 0
        countb = 0
        a = ['0'] * len(s)
        b = ['1'] * len(s)
        for i in range(0,len(s),2):
            a[i] = '1'
            b[i] = '0'
        for i in range(len(s)):
            if s[i] != a[i]:
                counta += 1
            if s[i] != b[i]:
                countb += 1
        return min(counta,countb)