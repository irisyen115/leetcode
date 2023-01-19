from collections import Counter

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        ans = []        
        for v in strs:
            c = Counter(v)
            s = ''
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if c[ch]:
                    s = s + ch + str(c[ch])
            if s not in d: d[s] = []
            d[s].append(v)
        for k,v in d.items():
            ans.append(v)
        return ans