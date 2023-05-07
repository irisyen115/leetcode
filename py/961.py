class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        n = len(nums) // 2
        for num in nums:
            if c[num] == n:
                return num
        