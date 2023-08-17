class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        return all((arr[i + 1] - arr[i]) == (arr[i + 2] - arr[i + 1]) for i in range(len(arr) - 2))