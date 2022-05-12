class Solution {
    public int countPrimes(int n) {
        int [] primes = new int[350000];
        primes [0] = 2;
        int count = 1;
       
        
        if (n <= 2) {
            return 0;
        }

        for (int i = 3; i < n; i+=2) {
            boolean found = true;
            for (int j = 0; j < count; j++) {    
                if (i < (primes[j] * primes[j])){
                    break;
                } 
                if (i % primes[j] == 0){
                    found = false;
                    break;
                }
            
                }
            

            if (found == true) {
            primes[count] = i;
            count++;
            }
        }
        
        return count;
    }
}
