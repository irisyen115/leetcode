class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        a = Counter(s1.split())
        b = Counter(s2.split())
        c = set(s1.split()) ^ set(s2.split())
        ans = []
        for v in c:
            if a[v] == 1 or b[v] == 1:
                ans.append(v)
        return ans