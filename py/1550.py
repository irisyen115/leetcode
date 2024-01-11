class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr) - 2):
            if all(v % 2 == 1 for v in [arr[i], arr[i+1], arr[i+2]]):
                return True
        return False