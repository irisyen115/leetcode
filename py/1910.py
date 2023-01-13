class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while True:
            if s.find(part) == -1:
                break
            s = s[:s.find(part)] + s[s.find(part)+len(part):]
        return s