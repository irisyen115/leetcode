class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans = []
        for query in queries:
            count, sm = 0, 0
            for i in range(len(nums)):
                if sm + nums[i] <= query:
                    sm += nums[i]
                    count += 1
            ans.append(count)
        return ans