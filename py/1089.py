class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0 and i < n:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 1
            i += 1
        