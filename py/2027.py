class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0        
        i = 0
        while i < len(s):
            if s[i] == 'X':
                i += 3    
                count += 1            
            else:
                i += 1
        return count