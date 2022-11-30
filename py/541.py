class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        ans = []
        head = 0
        tail = k
        for i in range(len(s)):
            if i == head:
                ans.extend(list(reversed(s[head:tail])))
            elif head < i < tail - 1:
                continue        
            elif i == tail -1 :
                head += 2 * k
                tail = head + k
            else:
                ans.append(s[i])

        return ''.join(ans)
        
