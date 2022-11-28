class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        return [k for k, v in Counter(s1.split() + s2.split()).items() if v == 1]