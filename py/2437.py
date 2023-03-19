class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        count = 1
        if time[0] == '?' and time[1] == '?':
            count *= 24
        elif time[0] == '?' and int(time[1]) < 4:
            count *= 3
        elif time[0] == '?' and int(time[1]) >= 4:
            count *= 2
        elif int(time[0]) >= 2 and time[1] == '?':
            count *= 4
        elif int(time[0]) < 2 and time[1] == '?':
            count *= 10
        if time[3] == '?':
            count *= 6
        if time[4] == '?':
            count *= 10
        return count