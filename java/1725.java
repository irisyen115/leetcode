class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int maxLen = 0;
        int count = 0;
        for(int[] rec:rectangles) {
            maxLen = Math.max(maxLen, Math.min(rec[0],rec[1]));            
        }
        
        for(int[] rec:rectangles) {            
            count+=(Math.min(rec[0],rec[1]) == maxLen ? 1:0);            
        }
        return count;
    }
}