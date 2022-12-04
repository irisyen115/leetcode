class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        w = {}
        for i in range(len(widths)):
            w[chr(97 + i)] = widths[i]
        p = 1
        ans = 0
        for v in s:      
            if ans + w[v] <= 100:
                ans += w[v]
            else:
                ans = w[v]            
                p += 1
        return [p,ans]        
