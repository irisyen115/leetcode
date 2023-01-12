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
            word, pos = q.popleft()
            a = pos
            q.append((s,a + 1))
            q.append((word,a + 1))    
            ans.add(word)
            if a >= len(s):
                while q:
                    word, pos = q.popleft()    
                    ans.add(word)
                break
            if word[pos].isalpha():
                low = word[:pos] + word[pos].lower() + word[pos+1:]
                up = word[:pos] + word[pos].upper() + word[pos+1:]
                q.append((low, a + 1))
                q.append((up, a + 1))
        return list(ans)