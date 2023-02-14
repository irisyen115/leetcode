class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """     
        st = ''   
        for i in range(len(s)-1):
            if s[i] == '1' and s[i+1] == '0':
                st = s[i+1:]
                break
        return '1' not in st
