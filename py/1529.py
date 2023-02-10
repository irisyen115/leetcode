class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        s = '0'  
        i = 0
        count = 0
        while i < len(target):
            if target[i] != s:
                if s == '0':
                    s = '1'            
                elif s == '1':
                    s = '0'
                count += 1
            i += 1
        return count