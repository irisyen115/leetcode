class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> res = new ArrayList<Boolean>();
        int max = 0;
        
        for(int candy: candies){
            if(candy > max){
                max = candy;
            }
        }
        
        for(int candy: candies){
            res.add(candy+extraCandies >= max);
        }
        return res;
    }
}
