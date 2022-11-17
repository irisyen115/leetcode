from collections import Counter

class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """        
        count = 0
        c1 = Counter(words1)
        c2 = Counter(words2)
        for a1,b1 in c1.items():
            for a2,b2 in c2.items():
                if a1 == a2 and b1 == b2 == 1:
                    count += 1
        return count