class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """       
        s = set() 
        while n > 1:
            a = 0            
            m = n
            while m > 0:
                a += (m % 10) ** 2
                m = m // 10
            if a in s:
                break        
            s.add(a)    
            n = a 
        return n == 1