class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        up, down, left, right = 0, n - 1, 0 , n - 1
        ans = [[0] * n for _ in range(n)]
        count = 1

        while up <= down and left <= right:
            for i in range(left, right + 1):
                ans[up][i] = count
                count += 1
            up += 1

            for i in range(up, down + 1):
                ans[i][right] = count
                count += 1
            right -= 1

            if up <= down:
                for i in range(right, left - 1, -1):
                    ans[down][i] = count
                    count += 1
                down -= 1

            if left <= right:
                for i in range(down, up - 1, -1):
                    ans[i][left] = count
                    count += 1
                left += 1
        return ans