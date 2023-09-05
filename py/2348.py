class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                count += (zero_count * (zero_count + 1)) // 2
                zero_count = 0

        count += (zero_count * (zero_count + 1)) // 2

        return count