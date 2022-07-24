public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int countA = countLength(headA);
        int countB = countLength(headB);
        while(countA != countB) {
            if(countA > countB) {
                headA = headA.next;
                countA--;
            } else {
                headB = headB.next;
                countB--;              
            }
        }        
        while(headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
    
    public int countLength(ListNode x) {
        int count = 0;        
        while(x != null) {
            x = x.next;
            count++;
        }
        return count;
    }
