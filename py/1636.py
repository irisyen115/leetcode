class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tup = []
        for v in set(nums):
            tup.append((nums.count(v), v))
        tup = sorted(tup, key=lambda num: (num[0], -num[1]))

        ans = []
        for a,b in tup:
            ans.extend([b] * a)

        return ans