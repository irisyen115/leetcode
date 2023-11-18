class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        swords = set([''.join(sorted(list(v))) for v in words])
        return len(words) - len(swords)