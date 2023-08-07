class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M = 0  
        far = 0  
        ans = 0  
        
        for i in range(len(nums) - 1):  
            M = max(M, i + nums[i])
            
            if i == far:
                far = M
                ans += 1
                
        return ans
