class Solution {
    public String reversePrefix(String word, char ch) {
        char[] a = word.toCharArray();
        String ans = ""; 
        int head = 0;
        char tmp;
        int tail = 0;        
        for(int i = 0; i < a.length; i++) {
            if(a[i] == ch) {
                tail = i;
                break;
            }             
        }
        while(head < tail) {
            tmp = a[head];
            a[head] = a[tail];
            a[tail] = tmp;
            head++;
            tail--;
        }
        for(char ch1:a) {
            ans += ch1;
        }
        return ans;
    }
}