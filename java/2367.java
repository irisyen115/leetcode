class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        int count = 0;
        HashSet<Integer> ans = new HashSet<Integer>();
        for(int num:nums) {
            ans.add(num);                        
        }
        
        for(int num:nums){
            if(ans.contains(num) && ans.contains(num + diff) && ans.contains(num + 2 * diff)) {
                count++;
            }
        }
        return count;
    }
}
