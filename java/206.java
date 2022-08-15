class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        ListNode tmp;
        while(cur != null) {
            tmp = cur.next;
            cur.next = prev;
            prev = cur;            
            cur = tmp;
        }
        return prev;
    }
}
