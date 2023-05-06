class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)
        s = set()
        for key,value in c.items():
            if value in s:
                return False
            s.add(value)
        return True