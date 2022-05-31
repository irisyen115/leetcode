class Solution {
    public char[] reverseString(char[] s) {
        for (int i = 0 ; i < s.length/2 ; i++) {
				char tmp = s[s.length-1-i];
				s[s.length-1-i] = s[i];
				s[i]= tmp;
		}
		return s;
    }
}
