bool isPalindrome(char * s){
    int length = strlen(s);
    char ans[length];
    int tail = 0;
    for(int i = 0; i < length; i++) {
        if(s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = s[i] + 32;
        }
        if(s[i] >= 'a' && s[i] <= 'z') {
            ans[tail] = s[i];
            tail++;
        } else if(s[i] >= '0' && s[i] <= '9') {
            ans[tail] = s[i];
            tail++;
        }
    }
    int head = 0;    
    tail-=1;
    while(head <= tail) {
        if(ans[head++] != ans[tail--]) {
            return false;
        }
    }
    return true;
}