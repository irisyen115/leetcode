class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        d = {v: i for i, v in enumerate(s)}
        for v in s:
            x = ord(v) - ord('a')
            if distance[x] != d[v]-s.index(v)-1:
                return False
        return True