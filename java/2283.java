class Solution {
    public boolean digitCount(String num) {
        int[] dic = new int[10];
        boolean check = false;
        for(char ch:num.toCharArray()) {
            dic[(int)ch-'0']+=1;
        }
        for(int i = 0; i < num.length(); i++) {
            if(num.charAt(i)-'0' == dic[i]) {
                check = true;
            } else {
                check = false;  
                break;
            }
        }
        return check;
    }
}