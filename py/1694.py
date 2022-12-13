class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        a = []
        for v in number:
            if v != ' ' and v != '-':
                a.append(v)
        ans = []
        b = 0
        for i in range(len(a)):            
            ans.append(a[i])
            b += 1            
            if b % 3 == 0:
                ans.append('-')
        print(ans)
        if ans[-1] == '-':
            return ''.join(ans[0:-1])
        elif ans[-2] == '-':
            ans.insert(-2,ans.pop(-2))
            return ''.join(ans)
        else:
            return ''.join(ans)