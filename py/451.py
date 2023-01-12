from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        sort = []
        c = Counter(s)
        for k,v in c.items():
            sort.append((v,k))
        sort = sorted((sort))[::-1]
        for a,b in sort:
            ans += b * a
        return ans