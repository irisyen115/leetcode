class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        ans = 0
        j = len(piles) - 1

        for i in range(len(piles) // 3):
            a = [piles[i], piles[j - 1], piles[j]]   
            ans += a[1]
            j -= 2

        return ans