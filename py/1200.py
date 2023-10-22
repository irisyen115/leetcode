class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        m = float('inf')
        for i in range(len(arr) - 1):           
            if (arr[i + 1] - arr[i]) < m:
                m = (arr[i + 1] - arr[i])
        for i in range(len(arr) - 1):           
            a = [] 
            if (arr[i + 1] - arr[i]) == m:
                a.extend([arr[i], arr[i + 1]])
            if a:
                ans.append(a)
        return ans