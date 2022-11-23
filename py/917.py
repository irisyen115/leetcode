class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        a = []
        for v in s:
            if (65 <= ord(v) <= 90) or (97 <= ord(v) <= 122):
                a.append(v)
        j = len(a)-1
        for i in range(len(s)):
            if (65 <= ord(s[i]) <= 90) or (97 <= ord(s[i]) <= 122):
                s[i] = a[j]
                j -= 1
        return ''.join(s)