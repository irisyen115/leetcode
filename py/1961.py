class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        head = 0
        for word in words:   
            if head >= len(s):
                return True         
            if s[head:head + len(word)] != word:
                return False
            head += len(word)         
        return ''.join(words) == s