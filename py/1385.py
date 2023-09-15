class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans = 0        
        for i in range(len(arr1)):
            dis = 1
            for j in range(len(arr2)):
                if (abs(arr1[i] - arr2[j]) <= d):
                    dis = 0
                    break
            ans += dis
        return ans