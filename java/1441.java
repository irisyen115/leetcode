class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> myList = new ArrayList<String>();
        int index = 1;
        while(index < target[target.length-1] + 1) {
            myList.add("Push");
            if(contains(target,index) == false) {
                myList.add("Pop");
            }
            index++;
        }
        return myList;
    }
    public static boolean contains(final int[] arr, final int key) {
        boolean found = false;
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == key) {
                found = true;
            }
        }
        return found; 
    }
}
