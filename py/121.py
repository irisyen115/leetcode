class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 1000000
        M = 0        
        for price in prices:
            m = min(m, price)
            M = max(M, price - m)
        return M