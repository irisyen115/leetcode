class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fm = sm = tm = float('-inf')
        i = 0
        while len(nums) > 0:
            if nums[i] > fm:
                tm = sm
                sm = fm
                fm = nums[i] 
            elif nums[i] > sm and nums[i] != fm:
                tm = sm
                sm = nums[i] 
            elif nums[i] > tm and nums[i] != sm and nums[i] != fm:
                tm = nums[i] 
            nums.pop(i)
        if sm == float('-inf') or tm == float('-inf'):
            return fm
        return tm