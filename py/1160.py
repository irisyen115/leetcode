class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """        
        count = 0
        for w in words:
            c = list(chars)        
            check = True
            for ch in w:
                if ch not in c:
                    check = False
                    break
                else:
                    c.remove(ch)
            if check:
                count += len(w)
        return count
            