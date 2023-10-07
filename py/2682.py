class Solution(object):
    def circularGameLosers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a = [0] * n
        i, r = 0, 1
        while True:
            if a[i] + 1 == 2:
                break
            a[i] += 1
            i = (i + (r * k)) % n
            r += 1
        return [i + 1 for i in range(len(a)) if a[i] == 0]