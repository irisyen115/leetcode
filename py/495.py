class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        time = 0
        for v in timeSeries:
            ans += (v + duration - max(v, time))
            time = (v + duration)
        return ans