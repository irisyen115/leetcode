class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """        
        ans = ''
        a = 0
        for i in range(len(str(n)) - 1, -1, -1):
            a += 1
            ans += str(n)[i]
            if a % 3 == 0 and i != 0:
                ans += '.'
        return ''.join(list(reversed(ans)))