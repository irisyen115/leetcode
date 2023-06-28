class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visit = set()

        d = {i:rooms[i] for i in range(len(rooms))}

        stack = [0]        
        while stack:
            cur = stack.pop()
            visit.add(cur)
            
            for n in d[cur]:
                if n not in visit:
                    stack.append(n)
        return len(visit) == len(rooms)