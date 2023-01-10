from collections import deque

class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """        
        q = deque([(s, 0)])
        ans = set()
        while q:            
            front = q.popleft()    
            a = front[1] + 1    
            q.append((s,a))
            q.append((front[0],a))    
            ans.add(front[0])
            if a > len(s):
                while q:
                    front = q.popleft()    
                    ans.add(front[0])
                break
            if front[0][front[1]].isalpha():
                if 65 <= ord(front[0][front[1]]) <= 90:
                    new_s = list(front[0])
                    new_s[front[1]] = new_s[front[1]].lower()            
                    new_s = ''.join(new_s)
                elif 97 <= ord(front[0][front[1]]) <= 122:
                    new_s = list(front[0])
                    new_s[front[1]] = new_s[front[1]].upper()            
                    new_s = ''.join(new_s)
                q.append((new_s,a))
        return list(ans)