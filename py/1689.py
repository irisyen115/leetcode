class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        M = -1
        for i in n:
            a = int(i)
            if a > M:
                M = a
        return M