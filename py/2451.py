class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        a = []
        d = {}
        for i,word in enumerate(words): 
            b = []
            for j in range(len(word)-1):
                b.append(abs(97 - ord(word[j+1])) - abs(97 - ord(word[j])))
            a.append(tuple(b))
            d[tuple(b)] = i
        c = Counter(a)
        for key,value in c.items():
            if value == 1: 
                return words[d[key]]          