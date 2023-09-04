class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        ans = []
        for num in nums:
            if num in s:
                ans.append(num)
            s.add(num)
        return ans