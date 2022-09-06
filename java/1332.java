class Solution {
    public int removePalindromeSub(String s) {
        char[] a = s.toCharArray();
        int head = 0;
        int tail = a.length-1;
        while(head < tail) {
            if(a[head++] != a[tail--]) {
                return 2;                
            }
        }
        return 1;
    }
}