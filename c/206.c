struct ListNode* reverseList(struct ListNode* head){
    struct ListNode * prev = NULL;
    struct ListNode * cur = head;
    struct ListNode * tmp;
    while(cur != NULL) {
        tmp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = tmp;
    }
    return prev;
}
