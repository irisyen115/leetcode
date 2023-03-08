class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        r = [releaseTimes[0]]
        for i in range(1, len(releaseTimes)):
            r.append(releaseTimes[i] - releaseTimes[i - 1])        
        a = max(r)
        ans = []
        for i in range(len(r)):
            if r[i] == a:
                ans.append(keysPressed[i])
        return max(ans)