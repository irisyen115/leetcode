class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s = list(s)
        i = 0
        while i < len(s):
            a = s.pop(0)
            s += a
            if ''.join(s) == goal:
                return True
            i += 1
        return False