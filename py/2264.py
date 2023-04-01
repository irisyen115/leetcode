class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        a = []
        for x, y in itertools.groupby(num):
            if len(list(y)) >= 3:
                a.append(int(x))        
        return str(max(a)) * 3 if a else ""