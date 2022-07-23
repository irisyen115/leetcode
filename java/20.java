class Solution {
    public boolean isValid(String s) {
        char[] ans = new char[s.length()];
        int top = -1;
        
        for(char ch:s.toCharArray()) {
            if(ch == '(' || ch == '[' || ch == '{') {
                ans[++top] = ch;
            } else {
                if(top == -1) {
                    return false;
                }
                if(ch == ')' && ans[top] != '(' ) {
                    return false;
                } else if (ch == ']' && ans[top] != '[') {
                    return false;
                } else if (ch == '}' && ans[top] != '{') {
                    return false;
                } else {
                    top--;
                }
            } 
        }       
        return top == -1;
    }
}
