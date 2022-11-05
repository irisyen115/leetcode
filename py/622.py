class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0] * k
        self.f = 0        
        self.r = -1
        self.next = 0
        self.capacity = k
        self.num = 0        

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.num >= self.capacity:            
            return False       
        self.q[self.next] = value
        self.r = (self.r + 1) % self.capacity
        self.next = (self.next + 1) % self.capacity             
        self.num += 1                
        return True  

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.num == 0:
            return False    
        self.f+= 1
        self.num -= 1        
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.num == 0:
            return -1            
        return self.q[self.f]

    def Rear(self):
        """
        :rtype: int
        """        
        if self.num == 0:
            return -1          
        return self.q[self.r]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.num == 0
            

    def isFull(self):
        """
        :rtype: bool
        """
        return self.num == self.capacity
            
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()