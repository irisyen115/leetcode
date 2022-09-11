class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        c=Counter(arr)   
        cur = 0;
        for i in arr:            
            if c[i] != 1:
                continue
            cur+=1
            if cur == k:
                return i
        return ""