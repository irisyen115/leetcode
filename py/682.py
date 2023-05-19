class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = []
        for v in operations:    
            if v == 'C':
                a.pop()
            elif v == 'D':
                a.append(a[-1] * 2)
            elif v == '+':
                a.append(a[-1] + a[-2])
            else:
                a.append(int(v))
        return sum(a)