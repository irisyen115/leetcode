class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        tail = nums[-k % len(nums):]
        head = nums[:-k % len(nums)]
        ans = tail + head
        for i in range(len(ans)):
            nums[i] = ans[i]