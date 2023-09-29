class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        ans = 0
        d = {}
        for domino in dominoes:
            sorted_d = tuple(sorted(domino))    

            if sorted_d in d:
                ans += d[sorted_d]
                d[sorted_d] += 1
            else:
                d[sorted_d] = 1
        return ans