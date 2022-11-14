class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        k = ''
        for v in key:
            if v not in k and v != ' ':
                k += v    
        ans = ''
        for v in message:
            if v == ' ':
                ans += v
            else:
                ans += chr(97 + (k.index(v)))
        return ans