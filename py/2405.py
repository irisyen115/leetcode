class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = []
        head = 1
        st = "" + s[0]
        while head <= len(s) - 1:
            if s[head] not in st:
                st += s[head]
                head += 1
            elif s[head] in st:                
                ans.append(st)
                st = ""
        if st:    
            ans.append(st)
        return len(ans)

