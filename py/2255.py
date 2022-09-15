class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for v in words:
            a = s[:len(v)]    
            if v == a:
                count += 1
        return count