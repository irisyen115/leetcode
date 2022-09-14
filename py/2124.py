class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for x, y in zip(s, s[1:]):
            if x == 'b' and y == 'a':
                return False
        return True