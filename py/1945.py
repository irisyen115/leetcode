class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s1 = ""
        for v in s:
            s1 += str(ord(v)-96)
        a = 0
        for i in range(k):
            while s1:
                a += int(s1) % 10    
                s1 = s1[:-1]
            s1 = str(a)
            a = 0
        return int(s1)
