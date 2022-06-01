class Solution {
    public char[] reverseString(char[] s) {
        int left = 0, right = s.length - 1;
        while(left < right) {
            char tmp = s[right];
            s[right] = s[left];
            s[left] = tmp;
            left++;
            right--;
        } 
		return s;
    }
}}
