class Solution {
    public String removeDuplicates(String s) {
        char[] a = s.toCharArray();
        char[] stack = new char[s.length()];
        int top = -1;
        String ans = "";
        
        for(int i = 0; i < a.length; i++) {
            if(top == -1 || a[i] != stack[top]) {
                top++;
                stack[top] = a[i]; 
            } else {
                top--;
            }                    
        }
        for(int i = 0; i <= top; i++) {
            ans += stack[i];
        }
        return ans;
    }
}
