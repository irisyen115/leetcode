class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = [s[0]]
        count = 0
        for i in range(1,len(s)):      
            if s[i-1] == s[i] :
                count += 1
            else:
                count = 0
            st.append(s[i])
            if count >= 2:
                st.pop()
        return ''.join(st)