class Solution {
    public char repeatedCharacter(String s) {
        char[] a = s.toCharArray();
        int[] b = new int[s.length()];
        for(int i = 0; i < a.length; i++) {
            for(int j = i+1; j < a.length; j++) {
                if(a[i] == a[j]) {
                    b[j] = j;
                }
            }
        }        
        Arrays.sort(b);
        for(int in:b) {
            if(in == 0) {
                continue;
            }
            return a[in];
        }
        return a[0];
    }
}
