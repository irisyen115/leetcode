class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """        
        d = Counter(words[0])
        ans = []
        for w in words[1:]:
            d = d & Counter(w) 
        for key,value in d.items():
            for _ in range(value):
                ans.append(key)
        return ans