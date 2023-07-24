class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0        
        j = nums[i]
        dj = {}
        if len(nums) == 1:
            return True
        while i < len(nums) - 1:
            if nums[i] == 0 and all(i >= key + value for key, value in dj.items()):
                return False        
            if i + nums[i] >= len(nums) - 1:
                return True 
            j = nums[i]                 
            dj[i] = j
            i += 1
        return False