class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """        
        return sum(startTime[i] <= queryTime <= endTime[i] for i in range(len(startTime)))