class Solution {
    public String destCity(List<List<String>> paths) {
        HashSet<String> start = new HashSet();
        HashSet<String> end = new HashSet();
        
        for(List<String> path:paths) {
            start.add(path.get(0));
            end.add(path.get(1));
        }
        
        end.removeAll(start);
        
        return end.iterator().next();
    }
}
