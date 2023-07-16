class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """   
        trans = []     
        for col in zip(*matrix):    
            trans.append(col[::-1])
        for i in range(len(matrix)):
            matrix[i] = trans[i]