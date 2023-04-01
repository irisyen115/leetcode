class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ans = []
        head = 0
        for x, y in itertools.groupby(s):
            tail = len(list(y))
            if tail >= 3:
                ans.append([head, head + tail - 1])
            head += tail
        return ans