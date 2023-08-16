class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        ans = []
        for word in words:
            ans.extend([v for v in word.split(separator) if v != ''])
        return ans