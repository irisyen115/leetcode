class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """               
        stack = []        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])                       
            elif s[i] == ')':     
                if '(' not in stack:
                    stack.append(s[i])                   
                else:
                    stack.remove('(')      
        return len(stack)