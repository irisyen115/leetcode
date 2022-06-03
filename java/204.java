class Solution {
    public int countPrimes(int n) {
        boolean []isprimes = new boolean[n+1];
        int count = 0;
        
        for(int i = 2; i < isprimes.length; i++){
            isprimes[i] = true;
        }
        
        for(int num = 2; num < n; num++){
            int mult = 2;
            if(!isprimes[num]){
                continue;
            }
            while(num * mult < isprimes.length){
                isprimes[num * mult] = false;
                mult++;
            }
            count++;
        }
        return count;        
    }
}
