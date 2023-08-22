class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        group = [(v, i) for i, v in enumerate(groupSizes)]
        group.sort()
        i = 0
        while group:
            a = group[0][0]
            ans.append([0] * a)
            j = 0
            while j < a:
                ans[i][j] = group[0][1]
                group.pop(0)
                j += 1
            i += 1
        return ans