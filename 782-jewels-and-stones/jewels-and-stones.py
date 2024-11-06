# from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set(jewels)
        counter = 0
        for s in stones:
            if s in jewelSet:
                counter += 1
        return counter