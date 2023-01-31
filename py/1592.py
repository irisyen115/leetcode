class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        s = 0
        for v in text:
            if v == ' ':
                s += 1
        text = text.split()
        if len(text) == 1 or (s // (len(text) - 1)) == 0:
            return ''.join(text) + s * ' '
        space = (s // (len(text) - 1)) * ' '        
        return space.join(text) + s % (len(text) - 1) * ' '