class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        trans = []     
        for col in zip(*matrix):    
            trans.append(col[::-1])

        rt = 0
        while rt < len(matrix):
            for i in range(1, len(matrix) + 1):
                if i not in matrix[rt] or i not in trans[rt]:
                    return False
            rt += 1
        return True