class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """        
        check = 0
        dic = [0,0,0,0,0,0,0,0,0,0]  
        for i in num:
            dic[int(i)]+=1
        for i in range(len(num)):
            if(int(num[i]) == dic[i]):
                check = 1
            else:
                check = 0
                break
        return check                