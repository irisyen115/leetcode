class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        z = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                z += 1
            else:
                i += 1
        return nums.extend([0] * z)