class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        count = 0
        for i in range(len(sequence) // len(word)):
            if word * (i + 1) in sequence:
                count += 1
        return count