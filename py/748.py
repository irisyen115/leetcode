class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        a = ""
        for v in licensePlate:
            if v.isalpha():
                a += v.lower()
        c = Counter(a)
        ans = []
        for word in words:
            if all(Counter(word)[x] >= c[x] for x,y in c.items()):
                ans.append(word)
        ans = sorted(ans, key=lambda x: len(x))
        return ans[0]