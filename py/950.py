class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        ans = []
        for v in deck:
            if len(ans) > 0:
                ans.insert(0, ans.pop())
            ans.insert(0, v)
        return ans