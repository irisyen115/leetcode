class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = [key for key, value in Counter(arr).items() if key == value]
        return -1 if not ans else max(ans)