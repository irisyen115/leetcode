class Solution(object):
    def countBeautifulPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x, y = nums[i], nums[j]
                while x >= 10:
                    x //= 10
                y  %= 10
                count += (gcd(x, y) == 1)
        return count