class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """        
        ans = [0] * len(boxes)
        ballsf = stepsf = 0
        ballsb = stepsb = 0
        front = [0] * len(boxes)
        back = [0] * len(boxes)
        for i in range(len(boxes)):
            stepsf += ballsf
            front[i] += stepsf
            ballsf += boxes[i] == '1'
        for i in range((len(boxes)-1),-1,-1):
            stepsb += ballsb
            back[i] += stepsb
            ballsb += boxes[i] == '1'
        for i in range(len(boxes)):
            ans[i] = front[i] + back[i]
        return ans
                        