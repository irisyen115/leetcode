class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = []
        sa = set()
        sb = set()

        for i in range(len(A)):
            sa.add(A[i])
            sb.add(B[i])
            count = len(sa & sb)
            ans.append(count)
        return ans