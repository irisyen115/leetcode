class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums:            
            num = str(num)
            while len(num) >= 2:                
                ans.append(int(num[0]))
                num = num[1:]
            ans.append(int(num))
        return ans