int getDecimalValue(struct ListNode* head){
    int sum = 0;
    struct ListNode* cur = head;
    while(cur != NULL) {
        sum = sum * 2 + cur->val;
        cur = cur->next;
    }
    return sum;
}
