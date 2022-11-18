class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Keyboard = {'qwertyuiop','asdfghjkl','zxcvbnm'}
        ans = []
        for word in words:
            for a in Keyboard:
                if all(v.lower() in a for v in word):
                    ans.append(word)
        return ans
        
