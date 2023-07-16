class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        trans = []
        ans = []
        for col in zip(*matrix):    
            trans.append(col)
            
        for row in range(len(matrix)):
            for i in range(len(matrix[row])):
                if matrix[row][i] == min(matrix[row]) and trans[i][row] == max(trans[i]):
                    ans.append(matrix[row][i])
        return ans