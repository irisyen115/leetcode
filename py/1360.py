class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def leap_year(b):
            c = 0    
            b1 = b[0]
            if (b[1] > 2) or (b[1] == 2 and b[2] == 29):b1 = b1 + 1
            for i in range(1972, b1, 4):
                if i % 100 == 0 and i % 400 != 0: continue
                c += 1                        
            return c        
        d1 = list(map(int, date1.split('-')))
        d2 = list(map(int, date2.split('-')))
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]                     
        count1 = ((d1[0] - 1970) * 365 + (sum(month[i] for i in range(d1[1] - 1))) + (d1[2] - 1) + leap_year(d1))
        count2 = ((d2[0] - 1970) * 365 + (sum(month[i] for i in range(d2[1] - 1))) + (d2[2] - 1) + leap_year(d2))
        return abs(count2 - count1)