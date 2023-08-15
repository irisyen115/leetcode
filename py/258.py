class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """ 
        ans = 0       
        while num > 0:
            ans += num % 10
            num = num // 10
            if num == 0 and ans > 0:
                if ans >= 10:
                    num = ans
                    ans = 0
                else:
                    break
        return ans