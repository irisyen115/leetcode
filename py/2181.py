# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = ListNode()
        dummy = ans

        count = 0
        while head:
            if head.val > 0:
                count += head.val
            if count > 0 and head.val == 0:
                node = ListNode(count)
                ans.next = node
                ans = ans.next
                count = 0
            head = head.next
        return dummy.next