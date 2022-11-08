class MyQueue(object):

    def __init__(self):
        self.x1 = []
        self.x2 = []
        self.num = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.x1.append(x)    
        self.num += 1

    def pop(self):
        """
        :rtype: int
        """  
        if self.empty():
            raise Exception
        self.num -= 1              
        if len(self.x2) == 0:            
            while self.x1:
                x = self.x1.pop()
                self.x2.append(x)
        return self.x2.pop()
        
    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            raise Exception
        if len(self.x2) == 0:            
            while self.x1:
                x = self.x1.pop()
                self.x2.append(x)        
        return self.x2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.num == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()