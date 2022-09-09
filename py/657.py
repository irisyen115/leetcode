class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """        
        up_down = 0
        left_right = 0
        for i in moves:
            if(i == 'U'):
                up_down+=1
            elif(i == 'D'):
                up_down-=1
            elif(i == 'L'): 
                left_right+=1
            else:
                left_right-=1
                    
        return (up_down == 0) and (left_right == 0)
                