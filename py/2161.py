class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left_nums = [v for v in nums if v < pivot]
        right_nums = [v for v in nums if v > pivot]
        nums = left_nums + [pivot] * nums.count(pivot) + right_nums
        return nums