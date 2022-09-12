class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        Glass = Paper = Metal = 0
        gi = pi = mi = 0
        for i,v in enumerate(garbage):            
            if 'G' in v:gi = i
            if 'P' in v:pi = i
            if 'M' in v:mi = i        
        for i in range(gi+1):
            Glass += (garbage[i].count('G'))
        for j in range(gi):
            Glass += travel[j]
        for i in range(pi+1):
            Paper += (garbage[i].count('P'))
        for j in range(pi):
            Paper += travel[j]
        for i in range(mi+1):
            Metal += (garbage[i].count('M'))
        for j in range(mi):
            Metal += travel[j]          
        return Glass + Paper + Metal