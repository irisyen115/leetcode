class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i = j = 0
        r = c = 0
        while i < len(matrix):
            while r + 1 < len(matrix) and c + 1 < len(matrix[i]):
                if matrix[r][c] == matrix[r + 1][c + 1]:
                    r += 1
                    c += 1
                else:
                    return False
            if j < len(matrix[i]) - 1:
                j += 1
            else:
                j = 0
                i += 1
            c = j          
            r = i
        return True