class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        ans = []
        head = 0
        while head < len(s):
            ans.append(s[head:head+k])
            head += k
        if len(ans[-1]) != k:
            ans[-1] = ans[-1] + (k - len(ans[-1])) * fill
        return ans