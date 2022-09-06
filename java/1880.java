class Solution {
  public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
      char[] a = firstWord.toCharArray();
      char[] b = secondWord.toCharArray();
      char[] c = targetWord.toCharArray();        
      int ac = 0;
      int bc = 0;
      int cc = 0;

      for(int i = 0; i < a.length; i++) {
          ac = ac * 10 +(int)(a[i]-'a');
      }

      for(int i = 0; i < b.length; i++) {
          bc = bc * 10 +(int)(b[i]-'a');
      }
      for(int i = 0; i < c.length; i++) {
          cc = cc * 10 +(int)(c[i]-'a');
      }
      return ac + bc == cc;
  }
}