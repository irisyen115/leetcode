class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        ans = [0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                ans[0] = mid
                break
                
        if nums and nums[ans[0]] == target:
            al = ans.pop()
            ar = al
            while al > 0 and nums[al - 1] == target:
                al -= 1
            while ar < len(nums) - 1 and nums[ar + 1] == target:
                ar += 1
            ans.extend([al, ar])
        else:
            ans = [-1, -1]
        return ans