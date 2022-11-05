# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """                
        dummy = ListNode('', head)
        prev = dummy
        cur = head
        while cur != None:
            if cur.val == val:
                prev.next = cur.next      
                cur = cur.next
            else:                          
                prev = prev.next
                cur = cur.next        
        return dummy.next
        