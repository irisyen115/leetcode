# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = ListNode()
        prev.next = cur
        dummy = prev

        if head == None:
            return None

        while cur and cur.next:
            if cur.val == cur.next.val:
                node = cur
                while node.val == cur.val:
                    if node.next:
                        node = node.next
                    else:
                        node = None
                        break
                prev.next = node       
                cur = node
            else:
                prev = prev.next
                cur = cur.next
        
        return dummy.next 