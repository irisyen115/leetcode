class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int count = 0;
        
        for(char jw:jewels.toCharArray()){
            for(char ch:stones.toCharArray()) {
                if(ch == jw) {
                    count++;
                }
            }
        }
        return count;
    }
}
