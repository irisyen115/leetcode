class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """        
        pairs = []
        for a, b in zip(s1, s2):
            if a != b:
                if len(pairs) == 2 : return False
                pairs.append((a, b))
        if len(pairs) == 2:
            (a, b), (c, d) = pairs
            return a == d and b == c
        return len(pairs) == 0
