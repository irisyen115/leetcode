class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        return sum((ord(list(reversed(columnTitle))[i]) - 65 + 1) * (26 ** i) for i in range(len(list(reversed(columnTitle)))))