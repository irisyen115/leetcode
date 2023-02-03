class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        n = str(n)         
        m = n
        if sum(int(v) for v in n) <= target:
            return 0
        else:            
            digit = 0
            while int(n) > target:
                n = str(int(n) // 10 + 1)     
                digit += 1
                if sum(int(v) for v in n) <= target:
                    return (10 ** digit) - int(m[len(m)-digit:])