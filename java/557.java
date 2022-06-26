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
        String ans = String.valueOf(ch);
        String[] wer = ans.split(" ");
        for(int i = 0; i < wer.length/2; i++){
            String tmp;
            tmp = wer[i];
            wer[i] = wer[wer.length-1-i];
            wer[wer.length-1-i] = tmp;
        }
        return String.join(" ",wer);
    }
}
