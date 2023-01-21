class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        k = []
        flag = ""
        count = 0
        ans = 0
        for ch in s:
            if ch != flag:
                k.append(count)
                flag = ch
                count = 1
            else:
                count += 1
        k.append(count)
        i = 1
        while i + 1 < len(k):
            ans += min(k[i], k[i + 1])
            i += 1
        return ans