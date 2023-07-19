# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        llen = 0      

        if head == None:
            return None

        while head:
            head = head.next
            llen += 1
            
        t = k % llen

        if t == 0:
            return cur

        k = llen - (k % llen)
        tail = cur
        head = ListNode()

        while k > 1:
            tail = tail.next
            k -= 1
        if k == 1:
            head = tail.next
            tail.next = None
                
        node = head
                
        while t > 1:
            node = node.next
            t -= 1
        if t == 1:
            node.next = cur
        return head