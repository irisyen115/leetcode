# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        carry = 0        

        while l1 or l2:            
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next
        
            total = total + carry
            cur.next = ListNode(total % 10)            
            carry = total // 10
            total = total % 10
            cur = cur.next
        
        if carry:
            cur.next = ListNode(carry)            

        return dummy.next