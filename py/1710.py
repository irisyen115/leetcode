class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        num = 0
        total = 0
        for boxes in boxTypes:
            if boxes[0] + num > truckSize:
                total += (truckSize - num) * boxes[1]
                break
            total += boxes[0] * boxes[1]
            num += boxes[0]
        return total