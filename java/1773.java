class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0;
        int index = 0;
        
        if(ruleKey.equals("type")) {
            index = 0;
        } else if(ruleKey.equals("color")) {
            index = 1;
        } else {
            index = 2;
        }
        
        for(int i = 0; i < items.size(); i++) {
            if(items.get(i).get(index).equals(ruleValue)) {
                count++;
            }
        }
        
        return count;
        
//         int count = 0;
//         int index = ruleKey.equals("type") ? 0 : ruleKey.equals("color") ? 1 : 2;
        
//         for (List<String> item : items) {
//             count += item.get(index).equals(ruleValue) ? 1 : 0;
//         }
        
//         return count;
    }
}
