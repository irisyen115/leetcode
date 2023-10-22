class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n

        A = min(op[0] for op in ops)
        B = min(op[1] for op in ops)

        return A * B