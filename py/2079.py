class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        cur = capacity
        steps = 1
        for i in range(1, len(plants)):
            cur -= plants[i - 1]
            if cur < plants[i]:
                steps += (i - 1 - (-1)) + ((i - (-1)))
                cur = capacity
            else:
                steps += 1
        return steps