class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """ 
        def gcd(a, b): 
            if (b == ""): 
                return a 
            if len(b) > len(a) : 
                return gcd(b, a)
            elif a[:len(b)] == b: 
                while a[:len(b)] == b:
                    a = a[len(b):]   
                return gcd(b, a)
            else:
                return ""  
        return gcd(str1, str2)