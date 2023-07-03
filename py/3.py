class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sub = []
        su = ''
        head = 0
        tail = 0
        i = 0
        while i < len(s):
            if s[i] in su:
                sub.append(len(su))
                head = s.index(s[i], head) + 1 
                su = ''
            else:
                tail += 1
                su = s[head:tail]
                i += 1
        sub.append(len(su))
        return max(sub)