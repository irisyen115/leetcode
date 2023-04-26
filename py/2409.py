class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        aA = sum(date[i] for i in range(int(arriveAlice.split('-')[0]) - 1)) + int(arriveAlice.split('-')[1])
        lA = sum(date[i] for i in range(int(leaveAlice.split('-')[0]) - 1)) + int(leaveAlice.split('-')[1])
        aB = sum(date[i] for i in range(int(arriveBob.split('-')[0]) - 1)) + int(arriveBob.split('-')[1])
        lB = sum(date[i] for i in range(int(leaveBob.split('-')[0]) - 1)) + int(leaveBob.split('-')[1])
        arrive = max(aA, aB)
        leave = min(lA, lB)
        if arrive > leave:
            return 0        
        return leave - arrive + 1
                