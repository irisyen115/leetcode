class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        occurance = [float("-inf")] + [i for i, v in enumerate(s) if v == c] + [float("inf")]
        ans = [] 
        occ_cur = 0
        occ_next = 1 
        for i in range(len(s)):
            if abs(occurance[occ_next] - i) < abs(i - occurance[occ_cur]): 
                occ_cur = occ_next 
                occ_next = occ_next + 1
            ans.append(abs(occurance[occ_cur] - i))
        return ans