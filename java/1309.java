class Solution {
    public String freqAlphabets(String s) {
        char[] a = s.toCharArray();
        String ans = "";
        int pos = 0;
        while(pos < a.length){
            if(a.length > pos + 2 && a[pos+2] == '#') {
                ans += (char)('a' + ((a[pos] - '0') * 10 + (a[pos + 1] -'0')) - 1 );
                pos += 3;
            } else {
                ans += (char)('a'+a[pos]-'0'-1);
                pos++;
            }
        }
        return ans;
    }
}
