class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        ans = []
        i = 0
        a = number
        while i < len(number):
            if number[i] == digit:
                number = list(number)
                number.pop(i)
                ans.append(int(''.join(number)))
                number = a
            i += 1
        return str(max(ans))