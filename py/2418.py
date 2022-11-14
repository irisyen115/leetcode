class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        nh = reversed(sorted(zip(heights,names)))
        return [b for _, b in nh]