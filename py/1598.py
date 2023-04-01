class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        count = 0
        for v in logs:
            if v[:-1] not in '..':
                count += 1
            elif v[:-1] == '..' and count > 0:
                count -= 1
        return count