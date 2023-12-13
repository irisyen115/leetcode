class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()        
        ans = sum(nums[:3])
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            cm = nums[i] + nums[i+1] + nums[i+2]
            cM = nums[i] + nums[-2] + nums[-1]
            if cm >= target:
                if abs(cm - target) < abs(ans - target):
                    return cm
                else: 
                    return ans
            if cM < target:
                if abs(cM - target) < abs(ans - target):
                    ans = cM
                continue
            
            j = i + 1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k] 
                if s == target:
                    return target
                if abs(target-s) < abs(target-ans):
                    ans = s
                
                if s < target:
                    j += 1
                else:
                    k -= 1
                
        return ans