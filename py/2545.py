class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        s = [(v[k], i) for i, v in enumerate(score)]
        s = sorted(s ,reverse=True)
        ans = []
        for a,b in s:
            ans.append(score[b])
        return ans