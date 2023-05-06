class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        totalTime = 0
        currX, currY = points[0][0], points[0][1]
        for i in range(1, len(points)):
            nextX, nextY = points[i][0], points[i][1]
            dx, dy = abs(nextX - currX), abs(nextY - currY)
            # 對角線移動需要sqrt(2)秒
            diagonalMoves = min(dx, dy)
            # 水平/垂直移動需要每單位1秒
            nonDiagonalMoves = abs(dx - dy)
            totalTime += diagonalMoves + nonDiagonalMoves
            currX, currY = nextX, nextY
        return totalTime