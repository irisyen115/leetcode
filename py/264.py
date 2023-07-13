class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """        
        ans = []
        seen = set()        
        ugly = [1]
        heapq.heapify(ugly)
        while len(ans) < n:
            f = heapq.heappop(ugly)
            ans.append(f)
            if f * 2 not in seen:
                heapq.heappush(ugly, f * 2)
            if f * 3 not in seen:
                heapq.heappush(ugly, f * 3)
            if f * 5 not in seen:
                heapq.heappush(ugly, f * 5)
            seen.add(f)
            seen.add(f * 2)
            seen.add(f * 3)
            seen.add(f * 5)

        return ans[n-1]