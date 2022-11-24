class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        a =[]
        b = set()
        for v in emails:
            a .append(  v.split("@"))
        for i in range(len(a)):
            if '.'  in  a[i][0]:
                a[i][0]=a[i][0].replace('.','')
            if '+' in a[i][0]:
                a[i][0]=a[i][0].replace(a[i][0][a[i][0].index('+'):len(a[i][0])],'')
            a[i] = a[i][0] + '@' + a[i][1]
            b.add(a[i])
        return len(b)
