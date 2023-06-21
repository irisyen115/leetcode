class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(map(str, nums))
        a = []
        for i in range(len(nums) // 2):
            a.append(nums[i] + nums[len(nums) - 1 -i])
        if len(nums) % 2 == 1:
            a.append(nums[len(nums) // 2])
        return sum(int(num) for num in a)