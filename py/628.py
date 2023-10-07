class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pos = [nums[i] for i in range(len(nums) - 1, len(nums) - 4, -1)]
        neg = [nums[i] for i in range(0, 3)]
                
        return max(pos[0] * pos[1] * pos[2], pos[0] * neg[0] * neg[1])
