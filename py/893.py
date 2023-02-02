class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """            
        return len(set( ''.join(sorted(word[::2])) + ''.join(sorted(word[1::2])) for word in words) )