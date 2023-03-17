class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """        
        m = {ch: i for i, ch in enumerate(order)}
        m[''] = -1
        for w1, w2 in zip(words, words[1:]):
            for ch1, ch2 in izip_longest(w1, w2, fillvalue=''):
                if m[ch1] < m[ch2]: break
                elif m[ch1] > m[ch2]: return False
        return True