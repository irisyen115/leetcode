class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] alphabet = new boolean[26];
        boolean found = false;
        for(char ch:sentence.toCharArray()) {
            alphabet[ch - 'a'] = true;
        }
        for(boolean bool:alphabet){
            if(bool == true){
                found = true;
            } else{
                found = false;
                break;
            }
        }
        return found;
    }
}
