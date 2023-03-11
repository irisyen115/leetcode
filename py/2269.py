class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        nums = str(num)
        count = 0
        for i in range(len(nums) - k + 1):
            a = int(nums[i:i + k])
            if a != 0:
                if num % a == 0:
                    count += 1
        return count