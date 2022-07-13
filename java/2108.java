class Solution {
    public String firstPalindrome(String[] words) {
        for(String st:words) {
            char[] ans = st.toCharArray();
            int left = 0;
            int right = ans.length - 1;
            while(left < right) {
                if(st.charAt(left) == st.charAt(right)) {
                    left++;
                    right--;                    
                } else {
                  break;
                }
            }
            if(left >= right) {
                return st;
            }
        }
        return "";
    }
}
