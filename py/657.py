class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = []
        
        for i in moves:
            a.append(i)
            
        up_down = 0
        left_right = 0
        
        for ch in a:
            if(ch == 'U'):
                up_down+=1
            elif(ch == 'D'):
                up_down-=1
            elif(ch == 'L'): 
                left_right+=1
            else:
                left_right-=1
                
        return (up_down == 0) and (left_right == 0)
                