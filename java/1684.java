class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        int count = 0;
        boolean[] dict = new boolean[26];
        for(char ch1:allowed.toCharArray()) {
            dict[ch1 - 'a'] = true;
        }
        
        for(String st:words) {
            boolean correct = true;
            for(char ch2:st.toCharArray()) {                
                if(dict[ch2- 'a'] == false){
                    correct = false;
                    break;
                } 
            }
            if (correct == true) {
                count++;
            }
        }

        return count;
    }
}
