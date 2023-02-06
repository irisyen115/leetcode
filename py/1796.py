class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = []
        for v in set(s):
            if v.isdigit():
                a.append(int(v))
        if len(a) > 1:
            return sorted(a)[-2]        
        else:
            return -1