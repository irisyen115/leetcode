class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a','e','i','o','u']
        head = 0
        tail = len(s)-1
        while head < tail:
            if s[head].lower() in vowels and s[tail].lower() in vowels:
                s[head],s[tail] = s[tail],s[head]                  
                head += 1
                tail -= 1
            if s[tail].lower() not in vowels:
                tail -= 1
            if s[head].lower() not in vowels:
                head += 1                  
        return ''.join(s)