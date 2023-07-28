class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0
        while i < n:
            new_num = 0
            num = nums[i]
            while num:
                new_num = new_num * 10 + num % 10
                num = num // 10
            nums.append(new_num)
            i += 1
        return len(set(nums))