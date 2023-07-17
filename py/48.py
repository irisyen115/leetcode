class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """   
        head = 0
        tail = len(matrix) - 1

        while head < tail:
            matrix[head], matrix[tail] = matrix[tail], matrix[head]
            head += 1
            tail -= 1
    
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
