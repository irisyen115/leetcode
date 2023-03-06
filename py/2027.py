class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = 0
        while i < len(s):   
            if i < len(s) - 2:
                if s[i] == 'X':
                    count += 1        
                    i += 3
                else:
                    i += 1
            else:            
                if i < len(s) - 1:    
                    if s[i] == 'X' or s[i+1] == 'X':                    
                        count += 1
                else:
                    if s[i] == 'X':                    
                        count += 1
                break
        return count