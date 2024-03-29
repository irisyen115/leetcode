# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  
        prev = None        
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        while prev:
            if prev.val == head.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True
