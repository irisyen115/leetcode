class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        k = {}
        ch = 0
        for v in key:
            if v not in k and v != ' ':
                k[v] = chr(97 + ch)
                ch += 1
        ans = ''
        for v in message:
            if v == ' ':
                ans += v
            else:
                ans += k[v]
        return ans