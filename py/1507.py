class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        ans = []
        d = date.split()
        Month = [("Jan",'01'), ("Feb",'02'), ("Mar",'03'), ("Apr",'04'), ("May",'05'), ("Jun",'06'), ("Jul",'07'), ("Aug",'08'), ("Sep",'09'), ("Oct",'10'), ("Nov",'11'), ("Dec",'12')]
        day = ''
        ans.append(d[2])
        for a,b in Month:
            if a == d[1]:
                ans.append(b)
                break
        for v in d[0]:
            if v.isdigit():
                day += v
            else:
                break
        if int(day) < 10:
            ans.append('0' + day)
        else:
            ans.append(day)
        return '-'.join(ans)