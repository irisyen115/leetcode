class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        return sum(min(abs(ord(a) - ord(b)), 26 - abs(ord(a) - ord(b))) for a, b in zip('a' + word, word)) + len(word)