class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """             
        a = m = sum(ch == 'W' for ch in blocks[:k])                        
        for tail in range(k, len(blocks)):
            a = a + (blocks[tail] == 'W') - (blocks[tail - k] == 'W')
            m = min(m, a)
        return m