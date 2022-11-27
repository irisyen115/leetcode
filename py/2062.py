class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        word = list(word)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        head = 0
        tail = 5
        count = 0
        while tail <= len(word):
            while tail <= len(word) and all(v in vowels for v in word[head:tail]):                
                if set(word[head:tail])  == vowels:
                    count += 1
                tail += 1
            head += 1
            tail = head + 5
        return count
