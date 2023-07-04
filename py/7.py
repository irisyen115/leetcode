class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            if int('-' + str(abs(x))[::-1]) < - (2 ** 31):
                return 0
            return int('-' + str(abs(x))[::-1])
        return 0 if int(str(abs(x))[::-1]) > (2 ** 31 - 1) else int(str(abs(x))[::-1])
