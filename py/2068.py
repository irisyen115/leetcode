class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        b1 = [0] * 26
        b2 = [0] * 26
        for v in word1:
            b1[ord(v) - 97] += 1
        for v in word2:
            b2[ord(v) - 97] += 1
        for i in range(26):
            if abs(b1[i] - b2[i]) > 3:
                return False
        return True