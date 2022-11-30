class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = []
        for v in s.split():
            if not v.isalpha():
                n.append(int(v))

        for i in range(len(n)-1):
            if n[i] >= n[i+1]:
                return False
        return True
