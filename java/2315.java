class Solution {
    public int countAsterisks(String s) {
        char[] ans = s.toCharArray();
        int count = 0;
        int brackets = 0;
        for(int i = 0; i < ans.length; i++) {
            if(ans[i] == '|'){
                brackets++;
            }
            if(ans[i] == '*' && brackets % 2 == 0){
                count++;
            }
        }
        return count;
    }
}

