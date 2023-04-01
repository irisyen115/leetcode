class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        for v in word:
            if v.isalpha():
                word = word.replace(v,' ')
        word = set(map(int, word.split()))
        return len(word)