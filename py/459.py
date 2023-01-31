class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """           
        for l in range (1, len(s) // 2 + 1):
            if len(s) % l != 0:
                continue
            else:
                head = 0                
                while head + l < len(s):
                    if s[head:head + l] != s[head + l:head + l + l]:
                        break
                    if s[head:head + l] == s[head + l:head + l + l] and head + l + l == len(s):
                        return True
                    head += l
        return False