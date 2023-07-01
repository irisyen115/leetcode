class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(arr2)):
            ans.extend([arr2[i]] * arr1.count(arr2[i]))
            arr1 = [v for v in arr1 if v != arr2[i]]
        return ans + sorted(arr1)