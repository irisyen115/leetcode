class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue            
                if words[i] in ans:
                    continue            
                if words[i] in words[j]:                    
                    ans.append(words[i])
        return ans                    