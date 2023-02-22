class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        c1 = Counter(s)
        c2 = Counter(target)
        m = 100000
        for key,value in c2.items():
            m = min(c1[key]//value, m)
        return m