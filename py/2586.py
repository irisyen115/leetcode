class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        mom = ['a','e','i','o','u']        
        return sum(words[i][0] in mom and words[i][-1] in mom for i in range(left,right+1))            