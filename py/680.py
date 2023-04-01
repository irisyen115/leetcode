class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        head, tail = 0, len(s) - 1
        while head < tail:               
            if s[head] == s[tail]: 
                head, tail = head + 1, tail -1
            else:
                x, y = s[head:tail], s[head + 1 : tail + 1]
                return x == x[::-1] or y == y[::-1]
        return True