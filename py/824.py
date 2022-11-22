class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowel = ['a','e','i','o','u']
        s = sentence.split()
        ans = ''
        for i,v in enumerate(s):    
            a = list(v)
            if a[0].lower() not in vowel:
                a.insert(len(a)-1, a.pop(0))
            v = ''.join(a)
            v += 'ma' + 'a' * (i+1)            
            ans += v + ' '
        return ans.strip()

