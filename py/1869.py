class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """                        
        M0 = -1
        M1 = -1
        count0 = 0
        count1 = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] == '0':
                    count0 += 1
                    M0 = max(M0, count0)
                    if s[i+1] == '1':
                        count0 = 0
                elif s[i] == '1':
                    count1 += 1
                    M1 = max(M1, count1)
                    if s[i+1] == '0':
                        count1 = 0                        
            else:
                if s[i] == '0':
                    count0 += 1
                    M0 = max(M0, count0)
                elif s[i] == '1':
                    count1 += 1
                    M1 = max(M1, count1)
        return M1 > M0