class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        items1 = sorted(items1)
        items2 = sorted(items2)
        a = [0] * max(items1[-1][0],items2[-1][0])
        ans = []
        for v in (items1 + items2):
            a[v[0]-1] += v[1]
        for i in range(len(a)):
            if a[i] != 0:
                ans.append([i+1,a[i]])
        return ans