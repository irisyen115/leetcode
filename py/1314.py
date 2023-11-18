class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            rhead = max(0, i - k)
            rtail = min(len(mat) - 1, i + k)        
            for j in range(len(mat[0])):
                chead = max(0, j - k)
                ctail = min(len(mat[0]) - 1, j + k)
                count = 0
                for r in range(rhead, rtail + 1):
                    for c in range(chead, ctail + 1):
                        count += mat[r][c]
                ans[i][j] = count
        return ans