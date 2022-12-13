class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        yd = [31,28,31,30,31,30,31,31,30,31,30,31]
        date = date.split('-')
        if int(date[0]) % 4 == 0:                    
            if int(date[0]) % 100 == 0:              
                if int(date[0]) % 400 == 0:          
                    yd[1] = 29
                else:
                    yd[1] = 28
            else:
                yd[1] = 29
        
        return sum(yd[i] for i in range(int(date[1]) -1)) + int(date[2])
        