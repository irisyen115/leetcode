class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower().replace(',',' ')                     
        paragraph = ''.join([v for v in paragraph if v.isalnum() or v == ' ']).split()
        i = 0
        while i < len(paragraph):
            if paragraph[i] in banned:
                paragraph.pop(i)
            else:
                i += 1
        return max(paragraph, key = paragraph.count)