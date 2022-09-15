class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0
        y = set(brokenLetters)
        for word in text.split( ):
            if len(set(word) & y) == 0:
                count+=1
        return count