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
        total_1 = ''
        total_2 = ''

        while l1 or l2:            
            if l1:
                total_1 += str(l1.val)
                l1 = l1.next

            if l2:
                total_2 += str(l2.val)
                l2 = l2.next
        
        total = int(total_1[::-1]) + int(total_2[::-1])

        if total == 0: 
            return cur

        while total:
            cur.next = ListNode(total % 10)
            total = total // 10
            cur = cur.next

        return dummy.next