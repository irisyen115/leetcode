class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for v in zip(*strs):
            for s1, s2 in zip(v, v[1:]):
                if ord(s1) > ord(s2):
                    count += 1
                    break
        return count