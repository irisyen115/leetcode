# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        cur = head

        while cur.next:
            node = ListNode(gcd(cur.val, cur.next.val))
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        return head