class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.remove(max(salary))
        salary.remove(min(salary))
        
        return float(sum(salary)) / float(len(salary))