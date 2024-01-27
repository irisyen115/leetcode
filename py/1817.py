class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        logs.sort()
        i = 0
        while i < len(logs):
            i += 1
            count = 0
            while i < len(logs) and logs[i][0] == logs[i - 1][0]:
                if logs[i][1] != logs[i - 1][1]:
                    # count 代表 UAM 的記數
                    # 若是使用者有不同的活躍分鐘數則count + 1
                    count += 1
                i += 1
            ans[count] += 1
        return ans 