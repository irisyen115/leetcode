class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)
        if binary[2] != '1':
            return False
        return '1' not in binary[3:]