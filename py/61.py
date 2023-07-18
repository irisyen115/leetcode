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
        dummy = ListNode()
        ans = ListNode()   
        ans = dummy
        node = head
        a = []
        if head == None:
            return None

        while node:
            a.append(node.val)
            node = node.next
            
        k = k % len(a)
            
        while a:
            while k:
                cur = ListNode(a.pop(-k))        
                ans.next = cur
                ans = ans.next
                k -= 1
            cur = ListNode(a.pop(0))
            ans.next = cur
            ans = ans.next
        return dummy.next