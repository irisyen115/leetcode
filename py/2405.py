class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """        
        head = 0
        st = set()
        count = 1
        while head < len(s):
            if s[head] not in st:
                st.add(s[head])
                head += 1
            elif s[head] in st:                
                count += 1
                st = set()        
        return count