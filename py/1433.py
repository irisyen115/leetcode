class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = sorted(s1)
        s2 = sorted(s2)
        a = []
        for i in range(len(s1)):
            if s1[i] != s2[i]: 
                a.append(ord(s1[i]) - ord(s2[i]))        
        if a[0] > 0:
            if any(v < 0 for v in a):
                return False
        elif a[0] < 0:
            if any(v > 0 for v in a):
                return False
        return True