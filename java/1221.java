class Solution {
    public int balancedStringSplit(String s) {
        char []chars = s.toCharArray();
        int count = 0;
        int diff = 0;
        
        for(char ch :chars){
            if(ch == 'R'){
                diff++;
            }
            if(ch == 'L'){
                diff--;
            }
            if(diff == 0){
                count++;
            }
        }
        return count;
    }
}
