class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """        
        return all(Counter(ransomNote)[x] <= Counter(magazine)[x] for x in set(ransomNote))