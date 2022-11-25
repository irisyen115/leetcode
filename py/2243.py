class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        while len(s) > k:
            head = 0
            tail = k
            a = []
            while tail < len(s):            
                a.append(''.join(s[head:tail]))
                head += k
                tail += k
            a.append(''.join(s[head:len(s)]))
            for i in range(len(a)):
                b = 0
                while int(a[i]) != 0:
                    b += int(a[i])%10
                    a[i] = int(a[i])//10
                a[i] = str(b)
            s = ''.join(a)
        ans = ''.join(s)
        return ans
