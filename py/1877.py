class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = float('-inf')
        
        while left < right:
            cur = nums[left] + nums[right]
            ans = max(ans, cur)
            left += 1
            right -= 1
        
        return ans