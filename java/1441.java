class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> a = new ArrayList<String>();
        int index = 0;
        int pos = 1;
        while(index < target.length) {
            a.add("Push");
            if(pos != target[index]) {
                a.add("Pop");
            } else {
                index++;
            }
            pos++;
        }
        return a;
    }
}
