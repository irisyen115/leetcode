class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        i, j  = 0, 0   
        c, d = i, j        
        s = set()
        while i < len(mat) and j < len(mat[0]):
            b = []    
            c, d = i, j        
            while c < len(mat) and d < len(mat[0]):
                if (c, d) in s:
                    break
                s.add((c, d))
                b.append(mat[c][d])
                c += 1
                d += 1
                if c >= len(mat) or d >= len(mat[0]):
                    a.append((sorted(b)))
                    break
            j += 1
            c, d = i, j        
            if j == len(mat[0]):
                j = 0
                i = i + 1
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        i, j  = 0, 0    
        for arr in a:
            if j >= len(ans[i]) or ans[i][j] != 0:
                j = 0
                i = i + 1
            c, d = i, j
            for v in arr:
                ans[c][d] = v
                c += 1
                d += 1
            j += 1
        return ans