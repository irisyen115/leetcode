class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [v for v in nums if v > 0]
        b = [v for v in nums if v < 0]
        ans = []
        for i in range(len(nums) // 2):
            ans.append(a[i])
            ans.append(b[i])
        return ans