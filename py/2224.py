class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """
        u = [int(v) for v in current.split(":")]
        o = [int(v) for v in correct.split(":")]
        count = 0
        t = 0
        if u[1] <= o[1]:
            count = o[0] - u[0]
            t = o[1] - u[1]            
        else:
            count = o[0] - u[0] - 1         
            t = o[1] + 60 - u[1]
        if t >= 15:            
            count += int(t // 15)
            t %= 15
        if t >= 5:
            count += int(t // 5)
            t %= 5
        count += t
        return count