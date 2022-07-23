class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dommy = new ListNode();
        ListNode prev = dommy;        
        while(list1 != null && list2 != null) {
            ListNode m = new ListNode();
            if(list1.val <= list2.val) {
                m.val = list1.val;
                list1 = list1.next;
            } else {
                m.val = list2.val;
                list2 = list2.next;
            }                        
            prev.next = m;
            prev = m;
        }                
        if(list1 == null) {
            prev.next = list2;
        } else {
            prev.next = list1;
        } 
        return dommy.next;
    }
}
