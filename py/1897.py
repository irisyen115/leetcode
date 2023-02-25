class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        def gcd(a,b): 
            if(b == 0): 
                return a 
            else: 
                return gcd(b , a % b) 
        if len(words) == 1:
            return True
        s = ""
        for word in words:
            s += word
        c = Counter(s)
        a = 0
        for key,value in c.items():             
            a = c[key]
            for key,value in c.items():             
                if gcd(a, value) == 1:
                    return False
        return True