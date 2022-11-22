def contains(container, contained):
    return all(container[x] >= contained[x] for x in contained)
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """     
        count = 0       
        c = Counter(chars)
        for v in words:
            d = Counter(v)
            if contains(c,d):
                count += len(v)
        return count