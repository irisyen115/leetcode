# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        fast = slow = head        
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        node = None        
        while slow != None:
            tmp = slow.next
            slow.next = node
            node = slow
            slow = tmp
        m = -1
        while node != None:
            if node.val + head.val > m:
                m = node.val + head.val
            node = node.next
            head = head.next
        return m

