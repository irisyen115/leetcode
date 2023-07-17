from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """        
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)

        for key, value in d.items():
            if len(value) > 1:
                for a,b in zip(value, value[1:]):
                    if b - a <= k:
                        return True
        return False