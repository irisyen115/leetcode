class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        ans = ""
        for v in title.split():
            if len(v) > 2:        
                ans += v[0].upper() + v[1:].lower()
            else:
                ans += v.lower()
            ans += " " 
        return ans[:-1]