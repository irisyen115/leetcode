class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        new_strs = []
        for v in zip(*strs):
            new_str = ""
            for s in v:
                new_str += s
            new_strs.append(new_str)
        for v in new_strs:
            for i in range(len(v)-1):
                if ord(v[i+1]) < ord(v[i]):
                    count += 1
                    break
        return count