class Solution {
    public String truncateSentence(String s, int k) {
        String []ans = new String[k];
        String[] xd = s.split(" ");

        for (int i = 0; i < k; i++) {
            ans[i] = xd[i];
        }
        return String.join(" ", ans);
    }
}
