class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        ans = []
        count = 0
        for i,ch in enumerate(pattern,1):
            if ch == 'I':
                ans.extend(range(i, i-count-1, -1))
                count = 0
            else:
                count += 1
            
        ans.extend(range(len(pattern)+1, len(pattern)+1-count-1, -1))
        return ''.join(map(str, ans))