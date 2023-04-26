class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = list(time)
        hign = "23:59"        
        if time[0] == '?' and time[1] != '?' and int(time[1]) >= 4:
            time[0] = '1'
        for i in range(len(time)):
            if time[i] == '?':   
                time[i] = hign[i]                                             
                if i == 1 and int(time[0]) == 2:
                    time[1] = hign[1]
                elif i == 1 and int(time[0]) < 2:
                    time[1] = '9'                            
        return ''.join(time)