class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """  
        s = [words[0]]      
        i = 1
        while i < len(words):
            s.append(words[i])
            if sorted(words[i-1]) == sorted(words[i]):                                 
                s.pop()
            i += 1 
        return s