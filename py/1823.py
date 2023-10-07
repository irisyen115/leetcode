class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        a = list(range(1, n + 1))
    
        i = 0
        
        while len(a) > 1:
            i = (i + k - 1) % len(a)
            
            del a[i]
        
        return a[0]
