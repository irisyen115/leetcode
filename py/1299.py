class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxRight = -1
        for i in range(len(arr)-1, -1, -1):
            a = arr[i]
            arr[i] = maxRight
            maxRight = max(a, maxRight)
        arr[-1] = -1
        return arr