class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        e = []
        o = []        
        for num in nums:
            if num % 2 == 1:
                o.append(num)
            else:
                e.append(num)

        ans = [0] * (len(nums)) 

        for i in range(len(ans) // 2):            
            ans[2 * i] = e[i]
            ans[2 * i + 1] = o[i]
        return ans