class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n <= 1:
            return True
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            planted += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            planted += 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                planted += 1
        return planted >= n