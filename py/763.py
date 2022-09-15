class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        d = {v: i for i, v in enumerate(s)}
        ans = []
        i = index = 0
        while index < len(s):
            a = d[s[index]]            
            while i < a:
                a = max(a,d[s[i+1]])               
                i+=1
            ans.append(a-index+1)
            index = a+1     
        return ans