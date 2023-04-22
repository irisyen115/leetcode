class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        c = []
        for i in range(len(mat)):
            if 1 in mat[i]:
                c.append([i,mat[i].count(1)])
        c = sorted(c, key=lambda c: c[1], reverse=True)
        return c[0] if c else [0,0]