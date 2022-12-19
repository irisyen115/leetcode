class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        c = Counter(text)
        a = Counter('balloon')
        ans = ''        
        for v in c:
            if v in a:
                if v == 'o' or v == 'l':
                    ans += (v * (c[v] // 2))
                else:
                    ans += (v * c[v])
        b = Counter(ans)        
        count = 10000        
        if all(v in ans for v in 'balloon'):
            for c,d in b.items():             
                if d < count:
                    count = d
        else:
            return 0
        return count

        