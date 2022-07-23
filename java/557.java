class Solution {
    public String reverseWords(String s) {
        char[] ch = s.toCharArray();
        int left = 0;
        int right = ch.length-1;
        char temp;
        while(right>left){
            temp = ch[left];
            ch[left] = ch[right];
            ch[right] = temp;
            right--;
            left++;
        }
        String[] ans = String.valueOf(ch).split(" ");
	left = 0;
	right = ans.length - 1;
	while (left < right) {
            String tmp = ans[left];
            ans[left] = ans[right];
            ans[right] = tmp;
	    left++; 
	    right--;
        }
        return String.join(" ",ans);
    }
}
