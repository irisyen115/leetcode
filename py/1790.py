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
        if len(pairs) == 1:
            return False
        elif len(s1) <= 2 and s1 != s2:
            return False
        elif len(pairs) == 2 and (pairs[0][0] != pairs[1][1] or pairs[0][1] != pairs[1][0]):
            return False
        else: 
            return True
