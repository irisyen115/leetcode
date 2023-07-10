class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if nums:
            head = 0
            tail = 0        
            for i in range(len(nums) - 1):
                if nums[i] + 1 != nums[i + 1]:
                    tail = i
                    if head == tail:
                        ans.append(str(nums[head]))
                    else:
                        ans.append(str(nums[head]) + "->" + str(nums[tail]))
                    head = i + 1
            tail = nums[-1]
            if nums[head] == tail:
                ans.append(str(tail))
            else:
                ans.append(str(nums[head]) + "->" + str(tail))
        return ans