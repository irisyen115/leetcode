from collections import Counter

class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        x, y = Counter(word1), Counter(word2)
        for i in range(26):
            if abs(x[chr(97 + i)] - y[chr(97 + i)]) > 3:
                return False
        return True