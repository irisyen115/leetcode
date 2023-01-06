class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max = -1
        for v in strs:
            if v.isdigit():
                if int(v) > max:
                    max = int(v)
            else:
                if len(v) > max:
                    max = len(v)
        return max