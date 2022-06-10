class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String ans1 = String.join("",word1);
        String ans2 = String.join("",word2);
        
        return ans1.equals(ans2);
    }
}
