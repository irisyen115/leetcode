class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        a = []
        for i in arr:
            if(arr.count(i) == 1):
                a.append(i)
        if(k-1 > len(a)) or (len(a) == 0):
            return ""
        else:
            return a[k-1]                    