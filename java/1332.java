class Solution {
    public int removePalindromeSub(String s) {
        char[] a = s.toCharArray();
        int head = 0;
        int tail = a.length-1;
        int count = 0;
        while(head < tail) {
            if(a[head] != a[tail]) {
                count = 2;
                break;
            } else {
                count = 1;                
            }
            head++;
            tail--;
        }
        return count;
    }
}