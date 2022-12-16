class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        s = set(list1) & set(list2) 
        s = list(s)
        m = 10000
        a = []
        ans = []
        for i,v in enumerate(s):
            if (list1.index(v) + list2.index(v)) <= m:
                m =list1.index(v) + list2.index(v)
        for i,v in enumerate(s):
            if (list1.index(v) + list2.index(v)) == m:
                a.append(i)        
        for i in a:
            ans.append(s[i])
        return ans