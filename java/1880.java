class Solution {
    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        char[] a = firstWord.toCharArray();
        char[] b = secondWord.toCharArray();
        char[] c = targetWord.toCharArray();        
        int ac = 0;
        int bc = 0;
        int cc = 0;

        for(int i = 0; i < a.length; i++) {
          ac += ((int)(a[i]-'a') * (Math.pow(10 , a.length-1-i)));
        }

        for(int i = 0; i < b.length; i++) {
          bc += ((int)(b[i]-'a') * (Math.pow(10 , b.length-1-i)));
        }
        for(int i = 0; i < c.length; i++) {
          cc += ((int)(c[i]-'a') * (Math.pow(10 , c.length-1-i)));
        }
        return ac + bc == cc;
    }
}