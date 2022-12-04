class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans = []
        def correspond(s):
            csd_d = {}
            csd_s = ''
            i = 0
            for v in s: 
                if v not in csd_d:
                    csd_d[v] = chr(i+97)
                    i += 1
                csd_s += csd_d[v]
            return csd_s

        for word in words:
            if correspond(word) == correspond(pattern):
                ans.append(word)
        return ans