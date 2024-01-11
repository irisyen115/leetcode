class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        ans = [0] * (len(pref))
        count = 0
        for i in range(len(pref)):
            ans[i] = count ^ pref[i]
            count ^= ans[i]
        return ans