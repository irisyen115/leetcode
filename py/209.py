class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        tail = 0
        ans = float('Inf')
        s = 0

        while tail < len(nums):
            s += nums[tail]

            while s >= target:
                ans = min(ans, tail - head + 1)
                s -= nums[head]
                head += 1

            tail += 1

        return 0 if ans == float('Inf') else ans