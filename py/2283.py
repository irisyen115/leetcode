class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        c=Counter(num)        
        for i,v in enumerate(num):            
            if v != str(c[str(i)]):
                return False            
        return True        