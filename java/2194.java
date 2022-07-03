class Solution {
    public List<String> cellsInRange(String s) {
        List<String> myList = new ArrayList<String>();
        char[] b = s.toCharArray();
        for(char x = b[0]; x <= b[3]; x++){
            for(char y = b[1]; y <= b[4]; y++) {
                myList.add(String.valueOf(x)+String.valueOf(y));
            }
        }
        return myList;
    }
}
