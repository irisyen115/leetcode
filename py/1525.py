class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        dl = {}
        dr = {} 
        count = 0  

        for i in range(len(s)):            
            if s[i] in dr:
                dr[s[i]] += 1
            else:
                dr[s[i]] = 1
            
        for i in range(len(s)):            
            if s[i] in dl:
                dl[s[i]] += 1                
            else:
                dl[s[i]] = 1
            
            dr[s[i]] -= 1
            
            if dr[s[i]] == 0:
                del dr[s[i]]
            
            if len(dl) == len(dr):
                count += 1

        return count