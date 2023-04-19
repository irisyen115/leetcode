import itertools

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """                
        a1 = [(x,len(list(y))) for x,y in itertools.groupby(name)]
        a2 = [(x,len(list(y))) for x,y in itertools.groupby(typed)]
        if len(a1) != len(a2):
            return False         
        for i in range(len(a1)):
            if a1[i][0] != a2[i][0]:
                return False
            elif a1[i][1] > a2[i][1]:
                return False
        return True