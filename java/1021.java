class Solution {
    public String removeOuterParentheses(String s) {
        String ans = "";
        int level = 0;
        for(char ch:s.toCharArray()) {
            if(ch == '(') {
                level++;
            } else {
                level--;
            }
            if(ch == '(' && level == 1) {
                continue;
            }
            if(ch == ')' && level == 0){
                continue;
            }
            ans += String.valueOf(ch);
        }
        return ans;
    }
}
